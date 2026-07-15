# Employee Attrition Data Engineering

![Python](https://img.shields.io/badge/Python-3.10-blue) ![Pandas](https://img.shields.io/badge/Pandas-2.x-green) ![SQLite](https://img.shields.io/badge/SQLite-Database-blue) ![Plotly](https://img.shields.io/badge/Plotly-Interactive-orange) ![License](https://img.shields.io/badge/License-MIT-success) ![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

*A Production-Ready Data Engineering Project for Employee Attrition Analysis using Python, SQL, SQLite, and Exploratory Data Analysis (EDA).*

---

## Project Overview

Employee attrition is one of the biggest challenges faced by Human Resource (HR) departments. Losing experienced employees increases recruitment costs, onboarding time, training expenses, and reduces overall organizational productivity.

This project demonstrates a complete production-style Data Engineering workflow using the IBM HR Analytics Employee Attrition & Performance dataset. The project covers data ingestion, validation, cleaning, transformation, feature engineering, SQL database integration, and Exploratory Data Analysis (EDA) to generate meaningful business insights.

This repository represents **Part 1** of the End-to-End Applied AI & ML Data Product Capstone Project.

---

## Repository

### Repository Name

`employee-attrition-data-engineering`

### Repository URL

https://github.com/pramodj551-oss/employee-attrition-data-engineering

### Repository Description

Production-ready Data Engineering project demonstrating ETL, Data Cleaning, SQL integration, Exploratory Data Analysis (EDA), and Business Insights using the IBM HR Analytics Employee Attrition dataset.

---

## Business Problem

Organizations need to answer two important analytical questions:

**Descriptive Analytics**
- What happened?

**Diagnostic Analytics**
- Why did it happen?

This project helps answer questions such as:

- Which department has the highest employee attrition?
- Does overtime increase employee turnover?
- Which age group experiences the highest attrition?
- Does monthly income affect employee retention?
- Which job roles require immediate HR attention?
- Does work-life balance influence attrition?
- How does job satisfaction impact employee retention?

---

## Project Objectives

- Build a production-ready Data Engineering pipeline.
- Load and validate raw employee data.
- Clean and preprocess the dataset.
- Handle missing values and duplicate records.
- Perform feature engineering.
- Store processed data in SQLite database.
- Perform SQL-based analysis.
- Generate interactive visualizations.
- Produce actionable business insights.
- Prepare high-quality data for Machine Learning (Part 2).

---

## Dataset

### Dataset Name

IBM HR Analytics Employee Attrition & Performance

### Source

IBM HR Analytics Sample Dataset (Available through public data repositories such as Kaggle)

### Dataset Statistics

| Attribute | Value |
|---|---|
| Total Records | 1470 |
| Total Features | 35 |
| Missing Values | 0 |
| Duplicate Records | 0 |

### Dataset Location

`data/raw/employee_attrition.csv`

---

## Repository Structure

```
employee-attrition-data-engineering/
│
├── data/
│   ├── raw/
│   │   └── employee_attrition.csv
│   ├── processed/
│   └── database/
│
├── notebooks/
│   └── Employee_Attrition_EDA.ipynb
│
├── outputs/
│   ├── charts/
│   ├── reports/
│   └── logs/
│
├── sql/
│   ├── create_tables.sql
│   ├── analysis_queries.sql
│   └── views.sql
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── logger.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── database.py
│   ├── eda.py
│   └── utils.py
│
├── tests/
│
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
└── main.py
```

---

## Technology Stack

- Python
- Pandas
- NumPy
- SQLite
- SQLAlchemy
- Matplotlib
- Plotly
- Seaborn
- Jupyter Notebook
- Git
- GitHub

---

## Key Features

- Production-ready Project Structure
- Data Loading Pipeline
- Dataset Validation
- Missing Value Handling
- Duplicate Removal
- Data Type Validation
- Feature Engineering
- Exploratory Data Analysis (EDA)
- SQLite Database Integration
- SQL Queries and Views
- Interactive Plotly Visualizations
- Logging System
- Business Reports

---

## Data Engineering Workflow

```
Raw Dataset
      │
      ▼
Data Loading
      │
      ▼
Data Validation
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Processed Dataset
      │
      ▼
SQLite Database
      │
      ▼
SQL Analysis
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Business Insights
```

---

## Exploratory Data Analysis (EDA)

The project includes:

- Dataset Overview
- Data Types Analysis
- Missing Value Analysis
- Duplicate Analysis
- Summary Statistics
- Department-wise Analysis
- Attrition Distribution
- Gender Analysis
- Monthly Income Analysis
- Job Satisfaction Analysis
- Work-Life Balance Analysis
- Overtime Analysis
- Correlation Heatmap
- Interactive Plotly Charts

---

## SQL Analysis

The SQL module provides:

- Employee Count
- Overall Attrition Rate
- Department-wise Attrition
- Gender-wise Attrition
- Job Role Analysis
- Monthly Income Analysis
- Experience Analysis
- Average Salary Analysis
- Aggregate Reports
- SQL Views

---

## Installation

### Clone Repository

```bash
git clone https://github.com/pramodj551-oss/employee-attrition-data-engineering.git
cd employee-attrition-data-engineering
```

### Create Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
python main.py
```

---

## Generated Outputs

After running the project, the following outputs are automatically generated:

- Cleaned Dataset
- SQLite Database
- Interactive Plotly Charts
- Correlation Heatmap
- Business Reports
- Application Logs

**Output Directories**

- `outputs/`
- `data/processed/`

---

## Sample Outputs

The project generates:

- Cleaned Employee Dataset
- Interactive Plotly Visualizations
- Correlation Heatmap
- SQLite Database
- Business Reports
- Log Files

---

## Business Insights

This analysis helps HR teams answer important business questions:

- Which employees are more likely to leave?
- Which departments experience higher attrition?
- Does overtime significantly increase employee turnover?
- Does salary influence employee retention?
- Which job roles require HR intervention?
- How does work-life balance affect attrition?
- Which employee groups require retention strategies?

---

## Future Improvements

- Automated ETL Pipeline
- Apache Airflow Integration
- Docker Containerization
- Cloud Database Support
- Power BI Dashboard
- Machine Learning Integration
- Real-Time Data Pipeline
- CI/CD Deployment

---

## Project Status

**Status:** ✅ Completed (Part 1)

**Completed Modules:**

- Data Engineering Pipeline
- Data Cleaning
- Data Validation
- Feature Engineering
- SQLite Integration
- SQL Analysis
- Exploratory Data Analysis
- Business Insights

**Next Repository:** Employee Attrition Prediction using Machine Learning (Part 2)

---

## Author

**Pramod Prakash Jadhav**

*AI/ML Developer | Security Analyst*

- 📧 Email: [pramodj551@gmail.com](mailto:pramodj551@gmail.com)
- 💼 LinkedIn: [pramod-prakash-jadhav-42ba2281](https://www.linkedin.com/in/pramod-prakash-jadhav-42ba2281)
- 💻 GitHub: [pramodj551-oss](https://github.com/pramodj551-oss)
- 📂 Project Repository: [employee-attrition-data-engineering](https://github.com/pramodj551-oss/employee-attrition-data-engineering)

---

## Connect with Me

- GitHub: [https://github.com/pramodj551-oss](https://github.com/pramodj551-oss)
- LinkedIn: [https://www.linkedin.com/in/pramod-prakash-jadhav-42ba2281](https://www.linkedin.com/in/pramod-prakash-jadhav-42ba2281)

I am passionate about Artificial Intelligence, Machine Learning, Data Engineering, Cybersecurity, and Data Analytics. This project demonstrates the design and implementation of a production-ready data engineering pipeline using Python, SQL, SQLite, and modern analytics tools.

---

## Acknowledgements

- IBM HR Analytics Dataset
- Pandas Documentation
- NumPy Documentation
- SQLAlchemy Documentation
- Plotly Documentation
- Matplotlib Documentation
- Seaborn Documentation
- Scikit-learn Documentation

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## Submission Checklist

- [x] Production-ready Folder Structure
- [x] Modular Python Code
- [x] Data Loading Pipeline
- [x] Data Cleaning & Validation
- [x] Feature Engineering
- [x] Exploratory Data Analysis (EDA)
- [x] SQLite Database Integration
- [x] SQL Queries & Views
- [x] Interactive Visualizations
- [x] Logging System
- [x] Professional Documentation
- [x] requirements.txt
- [x] MIT License
- [x] GitHub Ready Repository
- [x] Capstone Project Submission Ready
