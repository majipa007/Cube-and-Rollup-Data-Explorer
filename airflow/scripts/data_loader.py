import pandas as pd
import psycopg2
from psycopg2.extras import execute_batch

# Step 1: Read the CSV file
csv_file_path = "../data/Amazon Sale Report.csv"


print("data loaded successfully!")
def data_loader(csv_file_path):
    # Reading and cleaning the CSV
    data = pd.read_csv(csv_file_path)
    data = data.dropna()
    data = data.drop(columns=['Unnamed: 22', 'index', 'promotion-ids'])
    # Postgres Connection
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="database",
        user="postgres",
        password="secret"
    )
    # Insert Query
    cur = conn.cursor()
    insert_query = """
        INSERT INTO public.ecommerce_data (
            order_id, date, status, fulfilment, sales_channel, ship_service_level,
            style, sku, category, size, asin, courier_status, qty, currency, amount,
            ship_city, ship_state, ship_postal_code, ship_country, b2b, fulfilled_by
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    execute_batch(cur, insert_query, data.values.tolist())
    conn.commit()
    cur.close()
    conn.close()

data_loader(csv_file_path)