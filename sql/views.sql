-- ==========================================================
-- Employee Attrition Data Engineering Project
-- views.sql
--
-- Author : Pramod Prakash Jadhav
-- Database : SQLite
-- ==========================================================

-- Remove existing views
DROP VIEW IF EXISTS vw_employee_summary;
DROP VIEW IF EXISTS vw_department_summary;
DROP VIEW IF EXISTS vw_attrition_summary;
DROP VIEW IF EXISTS vw_salary_summary;
DROP VIEW IF EXISTS vw_jobrole_summary;
DROP VIEW IF EXISTS vw_overtime_summary;
DROP VIEW IF EXISTS vw_gender_summary;
DROP VIEW IF EXISTS vw_worklife_summary;

-- ==========================================================
-- View 1 : Employee Summary
-- ==========================================================

CREATE VIEW vw_employee_summary AS
SELECT
    EmployeeNumber,
    Age,
    Gender,
    Department,
    JobRole,
    MonthlyIncome,
    Attrition
FROM employee_attrition;

-- ==========================================================
-- View 2 : Department Summary
-- ==========================================================

CREATE VIEW vw_department_summary AS
SELECT
    Department,
    COUNT(*) AS TotalEmployees,
    ROUND(AVG(MonthlyIncome),2) AS AverageSalary,
    ROUND(AVG(JobSatisfaction),2) AS AverageJobSatisfaction
FROM employee_attrition
GROUP BY Department;

-- ==========================================================
-- View 3 : Attrition Summary
-- ==========================================================

CREATE VIEW vw_attrition_summary AS
SELECT
    Attrition,
    COUNT(*) AS TotalEmployees
FROM employee_attrition
GROUP BY Attrition;

-- ==========================================================
-- View 4 : Salary Summary
-- ==========================================================

CREATE VIEW vw_salary_summary AS
SELECT
    Department,
    MAX(MonthlyIncome) AS HighestSalary,
    MIN(MonthlyIncome) AS LowestSalary,
    ROUND(AVG(MonthlyIncome),2) AS AverageSalary
FROM employee_attrition
GROUP BY Department;

-- ==========================================================
-- View 5 : Job Role Summary
-- ==========================================================

CREATE VIEW vw_jobrole_summary AS
SELECT
    JobRole,
    COUNT(*) AS EmployeeCount,
    ROUND(AVG(MonthlyIncome),2) AS AverageSalary
FROM employee_attrition
GROUP BY JobRole;

-- ==========================================================
-- View 6 : Overtime Summary
-- ==========================================================

CREATE VIEW vw_overtime_summary AS
SELECT
    OverTime,
    Attrition,
    COUNT(*) AS EmployeeCount
FROM employee_attrition
GROUP BY OverTime, Attrition;

-- ==========================================================
-- View 7 : Gender Summary
-- ==========================================================

CREATE VIEW vw_gender_summary AS
SELECT
    Gender,
    COUNT(*) AS EmployeeCount,
    ROUND(AVG(MonthlyIncome),2) AS AverageSalary
FROM employee_attrition
GROUP BY Gender;

-- ==========================================================
-- View 8 : Work-Life Balance Summary
-- ==========================================================

CREATE VIEW vw_worklife_summary AS
SELECT
    WorkLifeBalance,
    COUNT(*) AS EmployeeCount,
    ROUND(AVG(JobSatisfaction),2) AS AverageJobSatisfaction
FROM employee_attrition
GROUP BY WorkLifeBalance;

-- ==========================================================
-- Verify Created Views
-- ==========================================================

SELECT name
FROM sqlite_master
WHERE type = 'view';
