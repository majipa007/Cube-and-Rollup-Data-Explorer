import pandas as pd
import psycopg2
from psycopg2.extras import execute_batch

# Step 1: Read the CSV file
csv_file_path = "Amazon Sale Report.csv"
data = pd.read_csv(csv_file_path)

data = data.dropna()
# Drop the unnecessary column
data = data.drop(columns=['Unnamed: 22', 'index', 'promotion-ids'])

# Step 2: Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="database",
    user="postgres",
    password="secret"
)
cur = conn.cursor()

# SQL INSERT Query
insert_query = """
    INSERT INTO public.ecommerce_data (
        order_id, date, status, fulfilment, sales_channel, ship_service_level,
        style, sku, category, size, asin, courier_status, qty, currency, amount,
        ship_city, ship_state, ship_postal_code, ship_country, b2b, fulfilled_by
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

# Use execute_batch for efficient bulk insertion
execute_batch(cur, insert_query, data.values.tolist())

# Commit the transaction
conn.commit()


# Step 4: Close the connection
cur.close()
conn.close()

print("Data loaded successfully!")