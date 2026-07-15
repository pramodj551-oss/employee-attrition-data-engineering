-- ==========================================================
-- Employee Attrition Data Engineering Project
-- analysis_queries.sql
--
-- Author : Pramod Prakash Jadhav
-- Database : SQLite
-- ==========================================================

-- ==========================================================
-- 1. Total Employees
-- ==========================================================

SELECT COUNT(*) AS Total_Employees
FROM employee_attrition;


-- ==========================================================
-- 2. Total Employees by Attrition
-- ==========================================================

SELECT
    Attrition,
    COUNT(*) AS Employee_Count
FROM employee_attrition
GROUP BY Attrition;


-- ==========================================================
-- 3. Department-wise Employee Count
-- ==========================================================

SELECT
    Department,
    COUNT(*) AS Employee_Count
FROM employee_attrition
GROUP BY Department
ORDER BY Employee_Count DESC;


-- ==========================================================
-- 4. Department-wise Attrition
-- ==========================================================

SELECT
    Department,
    Attrition,
    COUNT(*) AS Employee_Count
FROM employee_attrition
GROUP BY Department, Attrition
ORDER BY Department;


-- ==========================================================
-- 5. Gender-wise Attrition
-- ==========================================================

SELECT
    Gender,
    Attrition,
    COUNT(*) AS Employee_Count
FROM employee_attrition
GROUP BY Gender, Attrition;


-- ==========================================================
-- 6. Job Role-wise Attrition
-- ==========================================================

SELECT
    JobRole,
    Attrition,
    COUNT(*) AS Employee_Count
FROM employee_attrition
GROUP BY JobRole, Attrition
ORDER BY Employee_Count DESC;


-- ==========================================================
-- 7. Average Monthly Income
-- ==========================================================

SELECT
    ROUND(AVG(MonthlyIncome),2) AS Average_Monthly_Income
FROM employee_attrition;


-- ==========================================================
-- 8. Department-wise Average Salary
-- ==========================================================

SELECT
    Department,
    ROUND(AVG(MonthlyIncome),2) AS Average_Salary
FROM employee_attrition
GROUP BY Department
ORDER BY Average_Salary DESC;


-- ==========================================================
-- 9. Highest Paid Employees
-- ==========================================================

SELECT
    EmployeeNumber,
    JobRole,
    Department,
    MonthlyIncome
FROM employee_attrition
ORDER BY MonthlyIncome DESC
LIMIT 10;


-- ==========================================================
-- 10. Lowest Paid Employees
-- ==========================================================

SELECT
    EmployeeNumber,
    JobRole,
    Department,
    MonthlyIncome
FROM employee_attrition
ORDER BY MonthlyIncome ASC
LIMIT 10;


-- ==========================================================
-- 11. Overtime Analysis
-- ==========================================================

SELECT
    OverTime,
    Attrition,
    COUNT(*) AS Employee_Count
FROM employee_attrition
GROUP BY OverTime, Attrition;


-- ==========================================================
-- 12. Job Satisfaction Analysis
-- ==========================================================

SELECT
    JobSatisfaction,
    COUNT(*) AS Employees
FROM employee_attrition
GROUP BY JobSatisfaction
ORDER BY JobSatisfaction;


-- ==========================================================
-- 13. Work-Life Balance Analysis
-- ==========================================================

SELECT
    WorkLifeBalance,
    COUNT(*) AS Employees
FROM employee_attrition
GROUP BY WorkLifeBalance;


-- ==========================================================
-- 14. Marital Status Analysis
-- ==========================================================

SELECT
    MaritalStatus,
    Attrition,
    COUNT(*) AS Employee_Count
FROM employee_attrition
GROUP BY MaritalStatus, Attrition;


-- ==========================================================
-- 15. Education Field Analysis
-- ==========================================================

SELECT
    EducationField,
    COUNT(*) AS Employee_Count
FROM employee_attrition
GROUP BY EducationField
ORDER BY Employee_Count DESC;


-- ==========================================================
-- 16. Business Travel Analysis
-- ==========================================================

SELECT
    BusinessTravel,
    COUNT(*) AS Employee_Count
FROM employee_attrition
GROUP BY BusinessTravel;


-- ==========================================================
-- 17. Average Years at Company
-- ==========================================================

SELECT
    ROUND(AVG(YearsAtCompany),2) AS Avg_Years_At_Company
FROM employee_attrition;


-- ==========================================================
-- 18. Average Total Working Years
-- ==========================================================

SELECT
    ROUND(AVG(TotalWorkingYears),2) AS Avg_Total_Working_Years
FROM employee_attrition;


-- ==========================================================
-- 19. Performance Rating Distribution
-- ==========================================================

SELECT
    PerformanceRating,
    COUNT(*) AS Employee_Count
FROM employee_attrition
GROUP BY PerformanceRating;


-- ==========================================================
-- 20. Job Level Analysis
-- ==========================================================

SELECT
    JobLevel,
    COUNT(*) AS Employee_Count
FROM employee_attrition
GROUP BY JobLevel;


-- ==========================================================
-- 21. Environment Satisfaction
-- ==========================================================

SELECT
    EnvironmentSatisfaction,
    COUNT(*) AS Employee_Count
FROM employee_attrition
GROUP BY EnvironmentSatisfaction;


-- ==========================================================
-- 22. Relationship Satisfaction
-- ==========================================================

SELECT
    RelationshipSatisfaction,
    COUNT(*) AS Employee_Count
FROM employee_attrition
GROUP BY RelationshipSatisfaction;


-- ==========================================================
-- 23. Distance From Home
-- ==========================================================

SELECT
    ROUND(AVG(DistanceFromHome),2) AS Average_Distance
FROM employee_attrition;


-- ==========================================================
-- 24. Employees by Age
-- ==========================================================

SELECT
    Age,
    COUNT(*) AS Employee_Count
FROM employee_attrition
GROUP BY Age
ORDER BY Age;


-- ==========================================================
-- 25. Complete Department Summary
-- ==========================================================

SELECT
    Department,
    COUNT(*) AS Employees,
    ROUND(AVG(MonthlyIncome),2) AS Avg_Salary,
    ROUND(AVG(JobSatisfaction),2) AS Avg_Job_Satisfaction,
    ROUND(AVG(WorkLifeBalance),2) AS Avg_WorkLifeBalance
FROM employee_attrition
GROUP BY Department
ORDER BY Employees DESC;
