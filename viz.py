import streamlit as st
import pandas as pd
import plotly.express as px
import psycopg2

# Load the dataset
# Database connection details
DB_HOST = "localhost"  # Change if the database is on a different host
DB_PORT = "5432"
DB_NAME = "database"
DB_USER = "postgres"
DB_PASSWORD = "secret"

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

# Query to fetch data from the rollup table
region_based_sales = """
SELECT *
FROM public.region_based_sales;
"""

# Fetch data into a DataFrame
try:
    df = pd.read_sql_query(region_based_sales, conn)

    print("Data loaded successfully!")
except Exception as e:
    print(f"Error executing query: {e}")
finally:
    conn.close()
    print("Database connection closed.")


# Streamlit app
st.title("State-Level Rollup Data Visualization")

st.subheader("Data Overview")
st.dataframe(df)

# Sidebar Filters
st.sidebar.header("Filters")
selected_state = st.sidebar.selectbox("Select a State", df['ship_state'].unique())
selected_category = st.sidebar.selectbox("Select a Category", df['category'].unique())

# Filter data based on selection
filtered_data = df[
    (df['ship_state'] == selected_state) & (df['category'] == selected_category)
]

# Show filtered data
st.subheader("Filtered Data")
st.write(f"State: {selected_state} | Category: {selected_category}")
st.dataframe(filtered_data)

# Visualization 1: Total Sales by Category (Bar Chart)
st.subheader("Total Sales by State and Category")
fig1 = px.bar(
    df,
    x='ship_state',
    y='total_sales',
    color='category',
    title="Total Sales by State and Category",
    labels={'ship_state': 'State', 'total_sales': 'Total Sales'}
)
st.plotly_chart(fig1)

# Visualization 2: Order Count by State and Category (Stacked Bar Chart)
st.subheader("Order Count by State and Category")
fig2 = px.bar(
    df,
    x='ship_state',
    y='order_count',
    color='category',
    title="Order Count by State and Category",
    labels={'ship_state': 'State', 'order_count': 'Order Count'},
    barmode='stack'
)
st.plotly_chart(fig2)

# Visualization 3: Treemap for Total Sales
treemap_data = df.dropna(subset=['ship_country', 'ship_state', 'category'])

st.subheader("Treemap of Total Sales")
fig3 = px.treemap(
    treemap_data,
    path=['ship_country', 'ship_state', 'category'],  # Define the hierarchy
    values='total_sales',  # Values to size the treemap sections
    color='order_count',  # Optional: Color sections by order count
    color_continuous_scale='Viridis'  # Optional: Color scale
)
st.plotly_chart(fig3)
