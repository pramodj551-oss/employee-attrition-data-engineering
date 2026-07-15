"""
==========================================================
EDA Module
----------------------------------------------------------
Employee Attrition Data Engineering Project

Author : Pramod Prakash Jadhav
==========================================================

Description
-----------
This module performs Exploratory Data Analysis (EDA)
on the Employee Attrition dataset.

Features
--------
✔ Dataset Overview
✔ Summary Statistics
✔ Missing Value Analysis
✔ Data Type Analysis
✔ Duplicate Analysis
✔ Automatic Chart Saving
✔ Business Insights
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns

from src.config import CHARTS_DIR
from src.logger import logger

# ---------------------------------------------------------
# Plot Configuration
# ---------------------------------------------------------

plt.style.use("ggplot")

sns.set_theme(style="whitegrid")

# ---------------------------------------------------------
# EDA Class
# ---------------------------------------------------------


class EDA:
    """
    Exploratory Data Analysis Class.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Cleaned employee attrition dataset.
    """

    def __init__(self, dataframe: pd.DataFrame):

        self.df = dataframe.copy()

        logger.info("EDA Module Initialized.")

    # -----------------------------------------------------
    # Dataset Overview
    # -----------------------------------------------------

    def dataset_overview(self):
        """
        Display dataset overview.
        """

        logger.info("=" * 60)

        logger.info("DATASET OVERVIEW")

        logger.info("=" * 60)

        logger.info(f"Rows               : {self.df.shape[0]}")

        logger.info(f"Columns            : {self.df.shape[1]}")

        logger.info(
            f"Duplicate Records  : {self.df.duplicated().sum()}"
        )

        logger.info(
            f"Missing Values     : {self.df.isnull().sum().sum()}"
        )

        logger.info("=" * 60)

        print("\nFirst Five Records\n")

        print(self.df.head())

    # -----------------------------------------------------
    # Data Types
    # -----------------------------------------------------

    def data_types(self):
        """
        Display data types.
        """

        logger.info("Column Data Types")

        print("\n")

        print(self.df.dtypes)

    # -----------------------------------------------------
    # Dataset Information
    # -----------------------------------------------------

    def dataset_information(self):
        """
        Display dataframe information.
        """

        logger.info("Dataset Information")

        print("\n")

        self.df.info()

    # -----------------------------------------------------
    # Summary Statistics
    # -----------------------------------------------------

    def summary_statistics(self):
        """
        Display descriptive statistics.
        """

        logger.info("Generating Summary Statistics")

        print("\nNumerical Features\n")

        print(self.df.describe())

        print("\nCategorical Features\n")

        print(self.df.describe(include="object"))

    # -----------------------------------------------------
    # Missing Value Analysis
    # -----------------------------------------------------

    def missing_value_analysis(self):
        """
        Analyze missing values.
        """

        logger.info("Missing Value Analysis")

        missing = (
            self.df.isnull()
            .sum()
            .sort_values(ascending=False)
        )

        report = pd.DataFrame({
            "Missing Values": missing,
            "Percentage": (
                missing / len(self.df) * 100
            ).round(2)
        })

        print(report)

    # -----------------------------------------------------
    # Duplicate Analysis
    # -----------------------------------------------------

    def duplicate_analysis(self):
        """
        Display duplicate record count.
        """

        duplicates = self.df.duplicated().sum()

        logger.info(
            f"Duplicate Records : {duplicates}"
        )

        print(f"\nDuplicate Records : {duplicates}")

    # -----------------------------------------------------
    # Save Plot
    # -----------------------------------------------------

    def save_plot(
        self,
        figure_name: str
    ):
        """
        Save matplotlib figure.
        """

        output_file = Path(CHARTS_DIR) / figure_name

        plt.tight_layout()

        plt.savefig(
            output_file,
            dpi=300,
            bbox_inches="tight"
        )

        logger.info(
            f"Chart Saved : {output_file}"
)
      # -----------------------------------------------------
    # Attrition Distribution
    # -----------------------------------------------------

    def attrition_distribution(self):
        """
        Plot employee attrition distribution.
        """

        logger.info("Generating Attrition Distribution Chart")

        plt.figure(figsize=(8, 5))

        sns.countplot(
            data=self.df,
            x="Attrition"
        )

        plt.title("Employee Attrition Distribution")

        plt.xlabel("Attrition")

        plt.ylabel("Employee Count")

        self.save_plot("attrition_distribution.png")

        plt.close()

        # Interactive Plotly Chart
        fig = px.histogram(
            self.df,
            x="Attrition",
            color="Attrition",
            title="Employee Attrition Distribution"
        )

        fig.write_html(
            CHARTS_DIR / "attrition_distribution.html"
        )

    # -----------------------------------------------------
    # Department-wise Attrition
    # -----------------------------------------------------

    def department_attrition(self):
        """
        Department-wise employee attrition.
        """

        logger.info("Generating Department Attrition Chart")

        plt.figure(figsize=(10, 6))

        sns.countplot(
            data=self.df,
            x="Department",
            hue="Attrition"
        )

        plt.xticks(rotation=20)

        plt.title("Department-wise Attrition")

        self.save_plot("department_attrition.png")

        plt.close()

    # -----------------------------------------------------
    # Gender-wise Attrition
    # -----------------------------------------------------

    def gender_attrition(self):
        """
        Gender-wise attrition analysis.
        """

        logger.info("Generating Gender Attrition Chart")

        plt.figure(figsize=(7, 5))

        sns.countplot(
            data=self.df,
            x="Gender",
            hue="Attrition"
        )

        plt.title("Gender-wise Attrition")

        self.save_plot("gender_attrition.png")

        plt.close()

    # -----------------------------------------------------
    # Age Distribution
    # -----------------------------------------------------

    def age_distribution(self):
        """
        Age distribution of employees.
        """

        logger.info("Generating Age Distribution")

        plt.figure(figsize=(9, 5))

        sns.histplot(
            self.df["Age"],
            bins=20,
            kde=True
        )

        plt.title("Employee Age Distribution")

        plt.xlabel("Age")

        self.save_plot("age_distribution.png")

        plt.close()

    # -----------------------------------------------------
    # Education Analysis
    # -----------------------------------------------------

    def education_analysis(self):
        """
        Education field analysis.
        """

        logger.info("Generating Education Analysis")

        plt.figure(figsize=(11, 6))

        sns.countplot(
            data=self.df,
            x="EducationField"
        )

        plt.xticks(rotation=30)

        plt.title("Employees by Education Field")

        self.save_plot("education_analysis.png")

        plt.close()

    # -----------------------------------------------------
    # Marital Status Analysis
    # -----------------------------------------------------

    def marital_status_analysis(self):
        """
        Analyze marital status.
        """

        logger.info("Generating Marital Status Analysis")

        plt.figure(figsize=(8, 5))

        sns.countplot(
            data=self.df,
            x="MaritalStatus",
            hue="Attrition"
        )

        plt.title("Marital Status vs Attrition")

        self.save_plot("marital_status_analysis.png")

        plt.close()

    # -----------------------------------------------------
    # Business Insights
    # -----------------------------------------------------

    def business_insights_part1(self):
        """
        Generate basic business insights.
        """

        logger.info("=" * 60)

        logger.info("BUSINESS INSIGHTS - PART 1")

        logger.info("=" * 60)

        attrition_rate = (
            self.df["Attrition"]
            .value_counts(normalize=True) * 100
        ).round(2)

        print("\nOverall Attrition (%)")

        print(attrition_rate)

        print("\nDepartment-wise Attrition")

        print(
            pd.crosstab(
                self.df["Department"],
                self.df["Attrition"]
            )
        )

        print("\nGender-wise Attrition")

        print(
            pd.crosstab(
                self.df["Gender"],
                self.df["Attrition"]
            )
        )

        print("\nMarital Status vs Attrition")

        print(
            pd.crosstab(
                self.df["MaritalStatus"],
                self.df["Attrition"]
            )
        )

        logger.info("=" * 60)
      # -----------------------------------------------------
    # Monthly Income Analysis
    # -----------------------------------------------------

    def monthly_income_analysis(self):
        """
        Analyze employee monthly income.
        """

        logger.info("Generating Monthly Income Analysis")

        plt.figure(figsize=(10, 6))

        sns.histplot(
            self.df["MonthlyIncome"],
            bins=30,
            kde=True
        )

        plt.title("Monthly Income Distribution")

        plt.xlabel("Monthly Income")

        self.save_plot("monthly_income_distribution.png")

        plt.close()

    # -----------------------------------------------------
    # Overtime Analysis
    # -----------------------------------------------------

    def overtime_analysis(self):
        """
        Analyze overtime impact on attrition.
        """

        logger.info("Generating Overtime Analysis")

        plt.figure(figsize=(8, 5))

        sns.countplot(
            data=self.df,
            x="OverTime",
            hue="Attrition"
        )

        plt.title("OverTime vs Attrition")

        self.save_plot("overtime_analysis.png")

        plt.close()

    # -----------------------------------------------------
    # Job Satisfaction Analysis
    # -----------------------------------------------------

    def job_satisfaction_analysis(self):
        """
        Analyze job satisfaction.
        """

        logger.info("Generating Job Satisfaction Analysis")

        plt.figure(figsize=(8, 5))

        sns.countplot(
            data=self.df,
            x="JobSatisfaction",
            hue="Attrition"
        )

        plt.title("Job Satisfaction vs Attrition")

        self.save_plot("job_satisfaction_analysis.png")

        plt.close()

    # -----------------------------------------------------
    # Work-Life Balance Analysis
    # -----------------------------------------------------

    def work_life_balance_analysis(self):
        """
        Analyze work-life balance.
        """

        logger.info("Generating Work-Life Balance Analysis")

        plt.figure(figsize=(8, 5))

        sns.countplot(
            data=self.df,
            x="WorkLifeBalance",
            hue="Attrition"
        )

        plt.title("Work-Life Balance vs Attrition")

        self.save_plot("worklife_balance_analysis.png")

        plt.close()

    # -----------------------------------------------------
    # Job Role Analysis
    # -----------------------------------------------------

    def job_role_analysis(self):
        """
        Analyze employee job roles.
        """

        logger.info("Generating Job Role Analysis")

        plt.figure(figsize=(12, 6))

        sns.countplot(
            data=self.df,
            y="JobRole",
            hue="Attrition"
        )

        plt.title("Job Role vs Attrition")

        self.save_plot("job_role_analysis.png")

        plt.close()

    # -----------------------------------------------------
    # Business Travel Analysis
    # -----------------------------------------------------

    def business_travel_analysis(self):
        """
        Analyze business travel frequency.
        """

        logger.info("Generating Business Travel Analysis")

        plt.figure(figsize=(9, 5))

        sns.countplot(
            data=self.df,
            x="BusinessTravel",
            hue="Attrition"
        )

        plt.title("Business Travel vs Attrition")

        plt.xticks(rotation=15)

        self.save_plot("business_travel_analysis.png")

        plt.close()

    # -----------------------------------------------------
    # Monthly Income Boxplot
    # -----------------------------------------------------

    def income_boxplot(self):
        """
        Monthly income by attrition.
        """

        logger.info("Generating Income Boxplot")

        plt.figure(figsize=(8, 5))

        sns.boxplot(
            data=self.df,
            x="Attrition",
            y="MonthlyIncome"
        )

        plt.title("Monthly Income by Attrition")

        self.save_plot("income_boxplot.png")

        plt.close()

    # -----------------------------------------------------
    # Interactive Monthly Income Chart
    # -----------------------------------------------------

    def plotly_income_chart(self):
        """
        Interactive monthly income visualization.
        """

        logger.info("Generating Plotly Income Chart")

        fig = px.box(
            self.df,
            x="Attrition",
            y="MonthlyIncome",
            color="Attrition",
            title="Monthly Income vs Attrition"
        )

        fig.write_html(
            CHARTS_DIR / "monthly_income_plotly.html"
        )

    # -----------------------------------------------------
    # Interactive Department Chart
    # -----------------------------------------------------

    def plotly_department_chart(self):
        """
        Interactive department analysis.
        """

        logger.info("Generating Plotly Department Chart")

        fig = px.histogram(
            self.df,
            x="Department",
            color="Attrition",
            barmode="group",
            title="Department-wise Attrition"
        )

        fig.write_html(
            CHARTS_DIR / "department_attrition_plotly.html"
        )

    # -----------------------------------------------------
    # Business Insights - Part 2
    # -----------------------------------------------------

    def business_insights_part2(self):
        """
        Display additional business insights.
        """

        logger.info("=" * 60)

        logger.info("BUSINESS INSIGHTS - PART 2")

        logger.info("=" * 60)

        print("\nAverage Monthly Income by Attrition\n")

        print(
            self.df.groupby("Attrition")["MonthlyIncome"]
            .mean()
            .round(2)
        )

        print("\nAverage Job Satisfaction\n")

        print(
            self.df.groupby("Attrition")["JobSatisfaction"]
            .mean()
            .round(2)
        )

        print("\nAverage Work-Life Balance\n")

        print(
            self.df.groupby("Attrition")["WorkLifeBalance"]
            .mean()
            .round(2)
        )

        print("\nOverTime vs Attrition\n")

        print(
            pd.crosstab(
                self.df["OverTime"],
                self.df["Attrition"]
            )
        )

        print("\nBusiness Travel vs Attrition\n")

        print(
            pd.crosstab(
                self.df["BusinessTravel"],
                self.df["Attrition"]
            )
        )

        logger.info("=" * 60)
      # -----------------------------------------------------
    # Correlation Heatmap
    # -----------------------------------------------------

    def correlation_heatmap(self):
        """
        Generate correlation heatmap for numerical features.
        """

        logger.info("Generating Correlation Heatmap")

        plt.figure(figsize=(14, 10))

        correlation = self.df.select_dtypes(
            include=["number"]
        ).corr()

        sns.heatmap(
            correlation,
            cmap="coolwarm",
            annot=False,
            linewidths=0.5
        )

        plt.title("Correlation Heatmap")

        self.save_plot("correlation_heatmap.png")

        plt.close()

    # -----------------------------------------------------
    # Years At Company Analysis
    # -----------------------------------------------------

    def years_at_company_analysis(self):
        """
        Analyze YearsAtCompany vs Attrition.
        """

        logger.info("Generating YearsAtCompany Analysis")

        plt.figure(figsize=(10, 6))

        sns.boxplot(
            data=self.df,
            x="Attrition",
            y="YearsAtCompany"
        )

        plt.title("Years At Company vs Attrition")

        self.save_plot(
            "years_at_company_analysis.png"
        )

        plt.close()

    # -----------------------------------------------------
    # Job Level Analysis
    # -----------------------------------------------------

    def job_level_analysis(self):
        """
        Analyze Job Level vs Attrition.
        """

        logger.info("Generating Job Level Analysis")

        plt.figure(figsize=(8, 5))

        sns.countplot(
            data=self.df,
            x="JobLevel",
            hue="Attrition"
        )

        plt.title("Job Level vs Attrition")

        self.save_plot("job_level_analysis.png")

        plt.close()

    # -----------------------------------------------------
    # Department Salary Analysis
    # -----------------------------------------------------

    def department_salary_analysis(self):
        """
        Average Monthly Income by Department.
        """

        logger.info("Generating Department Salary Analysis")

        plt.figure(figsize=(10, 6))

        department_salary = (
            self.df.groupby("Department")["MonthlyIncome"]
            .mean()
            .sort_values()
        )

        department_salary.plot(
            kind="bar"
        )

        plt.title("Average Monthly Income by Department")

        plt.ylabel("Monthly Income")

        plt.xticks(rotation=20)

        self.save_plot(
            "department_salary_analysis.png"
        )

        plt.close()

    # -----------------------------------------------------
    # Attrition Pie Chart
    # -----------------------------------------------------

    def attrition_pie_chart(self):
        """
        Generate Attrition Pie Chart.
        """

        logger.info("Generating Attrition Pie Chart")

        attrition = (
            self.df["Attrition"]
            .value_counts()
        )

        plt.figure(figsize=(6, 6))

        plt.pie(
            attrition.values,
            labels=attrition.index,
            autopct="%1.1f%%",
            startangle=90
        )

        plt.title("Employee Attrition")

        self.save_plot("attrition_pie_chart.png")

        plt.close()

    # -----------------------------------------------------
    # Department Pie Chart
    # -----------------------------------------------------

    def department_pie_chart(self):
        """
        Department-wise employee distribution.
        """

        logger.info("Generating Department Pie Chart")

        department = (
            self.df["Department"]
            .value_counts()
        )

        plt.figure(figsize=(7, 7))

        plt.pie(
            department.values,
            labels=department.index,
            autopct="%1.1f%%"
        )

        plt.title("Department Distribution")

        self.save_plot(
            "department_distribution.png"
        )

        plt.close()

    # -----------------------------------------------------
    # Interactive Correlation Matrix
    # -----------------------------------------------------

    def plotly_correlation_matrix(self):
        """
        Interactive Correlation Heatmap.
        """

        logger.info(
            "Generating Interactive Correlation Matrix"
        )

        correlation = (
            self.df.select_dtypes(
                include=["number"]
            ).corr()
        )

        fig = px.imshow(
            correlation,
            text_auto=False,
            color_continuous_scale="RdBu_r",
            title="Interactive Correlation Matrix"
        )

        fig.write_html(
            CHARTS_DIR /
            "interactive_correlation_matrix.html"
        )

    # -----------------------------------------------------
    # Business Insights - Part 3
    # -----------------------------------------------------

    def business_insights_part3(self):
        """
        Generate additional business insights.
        """

        logger.info("=" * 60)

        logger.info("BUSINESS INSIGHTS - PART 3")

        logger.info("=" * 60)

        print("\nAverage Years At Company\n")

        print(
            self.df.groupby("Attrition")[
                "YearsAtCompany"
            ].mean().round(2)
        )

        print("\nAverage Job Level\n")

        print(
            self.df.groupby("Attrition")[
                "JobLevel"
            ].mean().round(2)
        )

        print("\nDepartment-wise Average Salary\n")

        print(
            self.df.groupby("Department")[
                "MonthlyIncome"
            ].mean().round(2)
        )

        print("\nCorrelation Matrix\n")

        print(
            self.df.select_dtypes(
                include=["number"]
            ).corr().round(2)
        )

        logger.info("=" * 60)
      # -----------------------------------------------------
    # Run Complete EDA Pipeline
    # -----------------------------------------------------

    def run(self):
        """
        Execute the complete Exploratory Data Analysis pipeline.
        """

        logger.info("=" * 70)
        logger.info("STARTING EXPLORATORY DATA ANALYSIS")
        logger.info("=" * 70)

        # Dataset Overview
        self.dataset_overview()

        self.dataset_information()

        self.data_types()

        self.summary_statistics()

        self.missing_value_analysis()

        self.duplicate_analysis()

        # Distribution Analysis
        self.attrition_distribution()

        self.department_attrition()

        self.gender_attrition()

        self.age_distribution()

        self.education_analysis()

        self.marital_status_analysis()

        # Employee Analysis
        self.monthly_income_analysis()

        self.overtime_analysis()

        self.job_satisfaction_analysis()

        self.work_life_balance_analysis()

        self.job_role_analysis()

        self.business_travel_analysis()

        self.income_boxplot()

        # Correlation Analysis
        self.correlation_heatmap()

        self.years_at_company_analysis()

        self.job_level_analysis()

        self.department_salary_analysis()

        self.attrition_pie_chart()

        self.department_pie_chart()

        # Interactive Plotly Charts
        self.plotly_income_chart()

        self.plotly_department_chart()

        self.plotly_correlation_matrix()

        # Business Insights
        self.business_insights_part1()

        self.business_insights_part2()

        self.business_insights_part3()

        logger.info("=" * 70)
        logger.info("EDA COMPLETED SUCCESSFULLY")
        logger.info("=" * 70)

        print("\n" + "=" * 70)
        print("EDA COMPLETED SUCCESSFULLY")
        print("Charts Saved Successfully")
        print(f"Charts Folder : {CHARTS_DIR}")
        print("=" * 70)


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    from src.data_loader import load_data
    from src.preprocessing import DataPreprocessor

    logger.info("=" * 70)
    logger.info("Employee Attrition EDA Testing")
    logger.info("=" * 70)

    # Load Dataset
    dataframe = load_data()

    # Preprocess Dataset
    processor = DataPreprocessor(dataframe)

    cleaned_dataframe = processor.process()

    # Run EDA
    analysis = EDA(cleaned_dataframe)

    analysis.run()

    logger.info("=" * 70)
    logger.info("EDA Testing Completed Successfully")
    logger.info("=" * 70)
