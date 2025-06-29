# sql-dw-repo
# 🏗️ Data Warehousing Project

This project implements a modern data warehousing solution by integrating structured data from two core enterprise systems — **ERP** and **CRM** — and leveraging an open data architecture using cutting-edge tools such as Apache Spark, Apache Airflow, MinIO, Apache Iceberg, and Grafana.

## 🚀 Overview

The goal of this project is to create a scalable, reliable, and analytics-ready data warehouse that enables efficient reporting and insights generation. The pipeline extracts, transforms, and loads (ETL) data from ERP and CRM sources, stores it in a data lake format, and exposes it for analytics and visualization.

## 🗂️ Data Sources

- **ERP System**: Contains business transaction data including finance, inventory, procurement, and sales.
- **CRM System**: Contains customer-related data including interactions, support tickets, marketing activity, and contact information.

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Apache Spark** | Distributed data processing for ETL pipelines |
| **Apache Airflow** | Workflow orchestration and scheduling |
| **MinIO** | S3-compatible object storage for the data lake |
| **Apache Iceberg** | High-performance table format for large-scale analytics |
| **Grafana** | Data visualization and monitoring |

## 🏗️ Architecture

1. **Data Ingestion**: 
   - Batch ingestion from ERP and CRM.
   - Raw data is uploaded to MinIO.

2. **Data Processing**:
   - Spark jobs clean, transform, and join ERP & CRM datasets.
   - Processed data is written in Iceberg format to MinIO.

3. **Workflow Orchestration**:
   - Apache Airflow manages and schedules the ETL pipelines.

4. **Data Storage**:
   - All data is stored in a **Data Lakehouse** architecture using MinIO and Iceberg.

5. **Analytics & Monitoring**:
   - Grafana dashboards built on top of queryable Iceberg tables for business KPIs and monitoring pipeline health.

## 🧱 Folder Structure

```bash
data-warehouse/
├── dags/                   # Airflow DAGs
├── spark-jobs/             # Spark ETL scripts
├── grafana/                # Grafana dashboards and configs
├── iceberg/                # Iceberg table definitions and configs
├── config/                 # Source configs, connection strings, secrets
└── README.md               # Project documentation

