CREATE MATERIALIZED VIEW mv_sales_summary AS
SELECT
    ship_country,
    ship_state,
    category,
    EXTRACT(MONTH FROM date) AS sale_month,
    SUM(amount) AS total_sales,
    COUNT(*) AS order_count
FROM public.ecommerce_data
GROUP BY ship_country, ship_state, category, EXTRACT(MONTH FROM date);

CREATE INDEX idx_mv_sales_summary_country
ON mv_sales_summary (ship_country);

CREATE INDEX idx_mv_sales_summary_category
ON mv_sales_summary (category);

CREATE INDEX idx_mv_sales_summary_month
ON mv_sales_summary (sale_month);

SELECT * FROM mv_sales_summary;
