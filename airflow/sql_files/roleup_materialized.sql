CREATE MATERIALIZED VIEW region_based_sales AS
SELECT
    ship_country,
    ship_state,
    category,
    SUM(amount) AS total_sales,
    COUNT(*) AS order_count
FROM public.ecommerce_data
GROUP BY ROLLUP(ship_country, ship_state, category)
ORDER BY ship_country, ship_state, category;

CREATE MATERIALIZED VIEW time_based_sales AS
SELECT
    EXTRACT(YEAR FROM date) AS year,
    EXTRACT(MONTH FROM date) AS month,
    ship_country,
    category,
    SUM(amount) AS total_sales,
    COUNT(*) AS order_count
FROM public.ecommerce_data
GROUP BY ROLLUP(EXTRACT(YEAR FROM date), EXTRACT(MONTH FROM date), ship_country, category)
ORDER BY year, month, ship_country, category;