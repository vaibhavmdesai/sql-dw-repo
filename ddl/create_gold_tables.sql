CREATE TABLE belong_iceberg_catalog.gold.dim_customers
(
customer_key integer,
customer_id integer,
customer_number varchar,
first_name varchar,
last_name varchar,
country varchar,
marital_status varchar,
gender varchar,
birth_date date,
create_date date,
dwh_load_date timestamp(6)
)
