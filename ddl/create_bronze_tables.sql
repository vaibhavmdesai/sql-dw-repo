create table belong_iceberg_catalog.bronze.crm_cust_info
(
cst_id integer,
cst_key varchar,
cst_firstname varchar,
cst_lastname varchar,
cst_marital_status varchar,
cst_gndr varchar,
cst_create_date date
);

create table belong_iceberg_catalog.bronze.crm_prd_info
(
prd_id integer,
prd_key varchar,
prd_nm varchar,
prd_cost double,
prd_line varchar,
prd_start_dt date,
prd_end_dt date
);

create table belong_iceberg_catalog.bronze.sales_details
(
sls_ord_num varchar,
sls_prd_key varchar,
sls_cust_id integer,
sls_order_dt integer,
sls_ship_dt integer,
sls_due_dt integer,
sls_sales double,
sls_quantity integer,
sls_price double
);

