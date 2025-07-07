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


CREATE TABLE belong_iceberg_catalog.gold.dim_products
(
product_key integer,
product_id integer,
product_number varchar,
product_name varchar,
category_id varchar,
category varchar,
subcategory varchar,
maintenance varchar,
cost double,
product_line varchar,
start_date varchar,
dwh_load_date timestamp(6)
);
