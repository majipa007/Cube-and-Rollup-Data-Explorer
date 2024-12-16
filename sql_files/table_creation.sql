CREATE TABLE ecommerce_data (
    index SERIAL PRIMARY KEY,
    order_id VARCHAR(50),
    date DATE,
    status VARCHAR(50),
    fulfilment VARCHAR(50),
    sales_channel VARCHAR(50),
    ship_service_level VARCHAR(50),
    style VARCHAR(50),
    sku VARCHAR(50),
    category VARCHAR(50),
    size VARCHAR(10),
    asin VARCHAR(50),
    courier_status VARCHAR(50),
    qty INT,
    currency VARCHAR(10),
    amount NUMERIC(10, 2),
    ship_city VARCHAR(100),
    ship_state VARCHAR(100),
    ship_postal_code VARCHAR(20),
    ship_country VARCHAR(50),
    b2b BOOLEAN,
    fulfilled_by VARCHAR(50)
);

select * from ecommerce_data limit 5;