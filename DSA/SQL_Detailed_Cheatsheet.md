# SQL Detailed Cheatsheet with Examples & Tricky Problems

A comprehensive guide to SQL with real-world examples, advanced techniques, and tricky interview problems.

---

## Table of Contents
1. [Basic SQL Syntax](#basic-sql-syntax)
2. [Data Types & Constraints](#data-types--constraints)
3. [CRUD Operations](#crud-operations)
4. [Joins & Relationships](#joins--relationships)
5. [Aggregate Functions](#aggregate-functions)
6. [Window Functions](#window-functions)
7. [Subqueries & CTEs](#subqueries--ctes)
8. [Advanced SQL Techniques](#advanced-sql-techniques)
9. [Performance Optimization](#performance-optimization)
10. [Tricky Interview Problems](#tricky-interview-problems)
11. [Real-World Scenarios](#real-world-scenarios)

---

## Basic SQL Syntax

### Database & Table Operations
```sql
-- Create database
CREATE DATABASE company_db;
USE company_db;

-- Create table with constraints
CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    hire_date DATE NOT NULL,
    salary DECIMAL(10,2) CHECK (salary > 0),
    department_id INT,
    manager_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

-- Create departments table
CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(50) NOT NULL UNIQUE,
    location VARCHAR(100),
    budget DECIMAL(12,2)
);

-- Create projects table
CREATE TABLE projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    project_name VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(12,2),
    status ENUM('Planning', 'Active', 'Completed', 'Cancelled') DEFAULT 'Planning'
);

-- Create employee_projects junction table
CREATE TABLE employee_projects (
    employee_id INT,
    project_id INT,
    role VARCHAR(50),
    hours_worked DECIMAL(5,2) DEFAULT 0,
    PRIMARY KEY (employee_id, project_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Alter table operations
ALTER TABLE employees ADD COLUMN bonus DECIMAL(8,2) DEFAULT 0;
ALTER TABLE employees MODIFY COLUMN phone VARCHAR(20);
ALTER TABLE employees DROP COLUMN bonus;
ALTER TABLE employees ADD INDEX idx_department (department_id);
ALTER TABLE employees ADD INDEX idx_salary (salary);
```

### Sample Data Insertion
```sql
-- Insert departments
INSERT INTO departments (department_name, location, budget) VALUES
('Engineering', 'San Francisco', 2000000.00),
('Marketing', 'New York', 800000.00),
('Sales', 'Chicago', 1200000.00),
('HR', 'Austin', 500000.00),
('Finance', 'Boston', 600000.00);

-- Insert employees
INSERT INTO employees (first_name, last_name, email, phone, hire_date, salary, department_id, manager_id) VALUES
('John', 'Doe', 'john.doe@company.com', '555-0101', '2020-01-15', 95000.00, 1, NULL),
('Jane', 'Smith', 'jane.smith@company.com', '555-0102', '2020-03-20', 87000.00, 1, 1),
('Mike', 'Johnson', 'mike.johnson@company.com', '555-0103', '2019-06-10', 92000.00, 1, 1),
('Sarah', 'Wilson', 'sarah.wilson@company.com', '555-0104', '2021-02-01', 78000.00, 2, NULL),
('David', 'Brown', 'david.brown@company.com', '555-0105', '2020-11-15', 85000.00, 2, 4),
('Lisa', 'Davis', 'lisa.davis@company.com', '555-0106', '2019-09-30', 110000.00, 3, NULL),
('Tom', 'Miller', 'tom.miller@company.com', '555-0107', '2021-05-12', 72000.00, 3, 6),
('Amy', 'Garcia', 'amy.garcia@company.com', '555-0108', '2020-08-25', 68000.00, 4, NULL),
('Chris', 'Martinez', 'chris.martinez@company.com', '555-0109', '2021-01-10', 75000.00, 5, NULL);

-- Insert projects
INSERT INTO projects (project_name, start_date, end_date, budget, status) VALUES
('Website Redesign', '2023-01-01', '2023-06-30', 150000.00, 'Active'),
('Mobile App', '2023-03-15', '2023-12-31', 300000.00, 'Active'),
('Data Migration', '2022-10-01', '2023-02-28', 80000.00, 'Completed'),
('Marketing Campaign', '2023-02-01', '2023-05-31', 120000.00, 'Active'),
('ERP Implementation', '2023-06-01', '2024-03-31', 500000.00, 'Planning');

-- Insert employee-project assignments
INSERT INTO employee_projects (employee_id, project_id, role, hours_worked) VALUES
(1, 1, 'Project Manager', 120.5),
(2, 1, 'Senior Developer', 180.0),
(3, 1, 'Developer', 160.0),
(1, 2, 'Technical Lead', 90.0),
(2, 2, 'Senior Developer', 200.0),
(4, 4, 'Marketing Manager', 150.0),
(5, 4, 'Marketing Specialist', 140.0),
(6, 3, 'Sales Lead', 100.0);
```

---

## CRUD Operations

### SELECT Statements
```sql
-- Basic SELECT
SELECT * FROM employees;
SELECT first_name, last_name, salary FROM employees;

-- SELECT with aliases
SELECT 
    first_name AS 'First Name',
    last_name AS 'Last Name',
    salary AS 'Annual Salary'
FROM employees;

-- SELECT with calculations
SELECT 
    first_name,
    last_name,
    salary,
    salary * 0.1 AS bonus,
    salary + (salary * 0.1) AS total_compensation
FROM employees;

-- DISTINCT values
SELECT DISTINCT department_id FROM employees;
SELECT DISTINCT department_id, manager_id FROM employees;

-- LIMIT and OFFSET
SELECT * FROM employees LIMIT 5;
SELECT * FROM employees LIMIT 5 OFFSET 10;  -- Skip first 10, get next 5
```

### WHERE Clause & Filtering
```sql
-- Basic WHERE conditions
SELECT * FROM employees WHERE salary > 80000;
SELECT * FROM employees WHERE department_id = 1;
SELECT * FROM employees WHERE hire_date >= '2020-01-01';

-- Multiple conditions
SELECT * FROM employees 
WHERE salary > 80000 AND department_id = 1;

SELECT * FROM employees 
WHERE salary > 90000 OR department_id = 3;

-- IN and NOT IN
SELECT * FROM employees 
WHERE department_id IN (1, 2, 3);

SELECT * FROM employees 
WHERE first_name NOT IN ('John', 'Jane');

-- BETWEEN
SELECT * FROM employees 
WHERE salary BETWEEN 70000 AND 90000;

SELECT * FROM employees 
WHERE hire_date BETWEEN '2020-01-01' AND '2020-12-31';

-- LIKE patterns
SELECT * FROM employees WHERE first_name LIKE 'J%';      -- Starts with J
SELECT * FROM employees WHERE last_name LIKE '%son';     -- Ends with son
SELECT * FROM employees WHERE email LIKE '%@company%';   -- Contains @company
SELECT * FROM employees WHERE first_name LIKE 'J___';    -- J followed by 3 chars

-- NULL handling
SELECT * FROM employees WHERE manager_id IS NULL;
SELECT * FROM employees WHERE manager_id IS NOT NULL;
SELECT * FROM employees WHERE phone IS NULL OR phone = '';

-- Regular expressions (MySQL)
SELECT * FROM employees WHERE first_name REGEXP '^[A-M]';  -- Names starting A-M
```

### INSERT, UPDATE, DELETE
```sql
-- INSERT single record
INSERT INTO employees (first_name, last_name, email, hire_date, salary, department_id)
VALUES ('Alice', 'Johnson', 'alice.johnson@company.com', '2023-01-15', 82000.00, 1);

-- INSERT multiple records
INSERT INTO employees (first_name, last_name, email, hire_date, salary, department_id) VALUES
('Bob', 'Williams', 'bob.williams@company.com', '2023-02-01', 79000.00, 2),
('Carol', 'Jones', 'carol.jones@company.com', '2023-02-15', 88000.00, 1),
('Dan', 'Taylor', 'dan.taylor@company.com', '2023-03-01', 76000.00, 3);

-- INSERT from SELECT
INSERT INTO high_earners (employee_id, full_name, salary)
SELECT employee_id, CONCAT(first_name, ' ', last_name), salary
FROM employees
WHERE salary > 90000;

-- UPDATE records
UPDATE employees 
SET salary = salary * 1.05 
WHERE department_id = 1;

UPDATE employees 
SET salary = 95000, department_id = 2 
WHERE employee_id = 5;

-- UPDATE with JOIN
UPDATE employees e
JOIN departments d ON e.department_id = d.department_id
SET e.salary = e.salary * 1.1
WHERE d.department_name = 'Engineering';

-- DELETE records
DELETE FROM employees WHERE employee_id = 10;

DELETE FROM employees 
WHERE hire_date < '2019-01-01' AND salary < 60000;

-- DELETE with JOIN
DELETE e FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE d.department_name = 'Temp';
```