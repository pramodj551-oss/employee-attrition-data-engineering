-- ==========================================================
-- Employee Attrition Data Engineering Project
-- create_tables.sql
--
-- Author : Pramod Prakash Jadhav
-- Database : SQLite
-- ==========================================================

-- Drop existing table if present

DROP TABLE IF EXISTS employee_attrition;

-- ==========================================================
-- Create Employee Attrition Table
-- ==========================================================

CREATE TABLE employee_attrition (

    Age INTEGER,

    Attrition TEXT,

    BusinessTravel TEXT,

    DailyRate INTEGER,

    Department TEXT,

    DistanceFromHome INTEGER,

    Education INTEGER,

    EducationField TEXT,

    EmployeeCount INTEGER,

    EmployeeNumber INTEGER PRIMARY KEY,

    EnvironmentSatisfaction INTEGER,

    Gender TEXT,

    HourlyRate INTEGER,

    JobInvolvement INTEGER,

    JobLevel INTEGER,

    JobRole TEXT,

    JobSatisfaction INTEGER,

    MaritalStatus TEXT,

    MonthlyIncome INTEGER,

    MonthlyRate INTEGER,

    NumCompaniesWorked INTEGER,

    Over18 TEXT,

    OverTime TEXT,

    PercentSalaryHike INTEGER,

    PerformanceRating INTEGER,

    RelationshipSatisfaction INTEGER,

    StandardHours INTEGER,

    StockOptionLevel INTEGER,

    TotalWorkingYears INTEGER,

    TrainingTimesLastYear INTEGER,

    WorkLifeBalance INTEGER,

    YearsAtCompany INTEGER,

    YearsInCurrentRole INTEGER,

    YearsSinceLastPromotion INTEGER,

    YearsWithCurrManager INTEGER

);

-- ==========================================================
-- Create Useful Indexes
-- ==========================================================

CREATE INDEX IF NOT EXISTS idx_department
ON employee_attrition(Department);

CREATE INDEX IF NOT EXISTS idx_attrition
ON employee_attrition(Attrition);

CREATE INDEX IF NOT EXISTS idx_gender
ON employee_attrition(Gender);

CREATE INDEX IF NOT EXISTS idx_jobrole
ON employee_attrition(JobRole);

CREATE INDEX IF NOT EXISTS idx_overtime
ON employee_attrition(OverTime);

CREATE INDEX IF NOT EXISTS idx_income
ON employee_attrition(MonthlyIncome);

CREATE INDEX IF NOT EXISTS idx_age
ON employee_attrition(Age);

-- ==========================================================
-- Verify Table
-- ==========================================================

SELECT name
FROM sqlite_master
WHERE type='table';

PRAGMA table_info(employee_attrition);
