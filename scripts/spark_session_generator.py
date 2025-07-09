from app_constants import *
from pyspark.sql import SparkSession

def create_spark_session():
    
    spark = SparkSession.builder \
    .appName("IcebergAsDefaultCatalog") \
    .config('spark.jars.packages', 
            'org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0,'
            'org.apache.iceberg:iceberg-spark-runtime-3.3_2.12:1.3.1,'
            'software.amazon.awssdk:bundle:2.17.178,'
            'software.amazon.awssdk:url-connection-client:2.17.178') \
    .config('spark.sql.extensions', 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions') \
    .config(f"spark.sql.catalog.{ICEBERG_CATALOG}", "org.apache.iceberg.spark.SparkCatalog") \
    .config(f"spark.sql.catalog.{ICEBERG_CATALOG}.type", "hive") \
    .config(f"spark.sql.catalog.{ICEBERG_CATALOG}.uri", HIVE_URI) \
    .config(f"spark.sql.catalog.{ICEBERG_CATALOG}.warehouse", f"s3a://{MINIO_DATA_BUCKET}/") \
    .config("spark.hadoop.fs.s3a.endpoint", MINIO_ENDPOINT) \
    .config("spark.hadoop.fs.s3a.access.key", MINIO_ACCESS_KEY) \
    .config("spark.hadoop.fs.s3a.secret.key", MINIO_SECRET_KEY) \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.hive.metastore.sasl.enabled", "false") \
    .config("spark.sql.iceberg.handle-timestamp-without-timezone", "true") \
    .getOrCreate()

    return spark