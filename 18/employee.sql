-- this is a SQL comment
-- first, tell SQLite3 to put headers on the output
.headers on
-- next, tell SQLite3 to output tab delimeted tables
.mode tabs

-- create our tables

CREATE TABLE department
(
		 DepartmentID INT,
		 DepartmentName VARCHAR(20)
);
 
CREATE TABLE employee
(
		 LastName VARCHAR(20),
		 DepartmentID INT
);

-- put some data into them

INSERT INTO department VALUES(31, 'Sales');
INSERT INTO department VALUES(33, 'Engineering');
INSERT INTO department VALUES(34, 'Clerical');
INSERT INTO department VALUES(35, 'Marketing');
 
INSERT INTO employee VALUES('Rafferty', 31);
INSERT INTO employee VALUES('Jones', 33);
INSERT INTO employee VALUES('Heisenberg', 33);
INSERT INTO employee VALUES('Robinson', 34);
INSERT INTO employee VALUES('Smith', 34);
INSERT INTO employee VALUES('Williams', NULL);

-- do a select

SELECT 'INNER JOIN';

SELECT LastName, DepartmentName
	FROM Employee
	JOIN Department 
		ON Employee.DepartmentID =
					Department.DepartmentID
;

SELECT 'LEFT JOIN';

SELECT LastName, DepartmentName
	FROM Employee
	LEFT JOIN Department 
		ON Employee.DepartmentID =
					Department.DepartmentID
;
