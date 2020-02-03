DROP TABLE IF EXISTS Cohorts;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Instructors;
DROP TABLE IF EXISTS Exercises;
DROP TABLE IF EXISTS Student_Exercise;

-- cohort table
CREATE TABLE 'Cohorts' (
	'Cohort_Id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'Cohort_Name' 		TEXT NOT NULL UNIQUE
);

-- student table
CREATE TABLE 'Students' (
	'Student_Id' 	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'First_Name' 	TEXT NOT NULL,
	'Last_Name' 	TEXT NOT NULL,
	'Slack_Handle' TEXT NOT NULL UNIQUE,
	'Cohort_Id' INTEGER,
	FOREIGN KEY('Cohort_Id') REFERENCES 'Cohorts'('Cohort_Id')  
	);

-- instructor table
CREATE TABLE 'Instructors' (
	'Instructor_Id' 			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'First_Name' 	TEXT NOT NULL,
	'Last_Name' 	TEXT NOT NULL,
	'Slack_Handle' TEXT NOT NULL UNIQUE,
	'Specialty' 	TEXT NOT NULL,
	'Cohort_Id' INTEGER,
	FOREIGN KEY('Cohort_Id') REFERENCES 'Cohorts'('Cohort_Id') 
);

-- exercises table
CREATE TABLE 'Exercises' (
	'Exercise_Id' 			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'Exercise_Name' 		TEXT NOT NULL UNIQUE,
	'Exercise_Language'  	TEXT NOT NULL
);

-- student_exercise table
CREATE TABLE 'Student_Exercise' (
	'Student_Exercise_Id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'Exercise_Id' INTEGER,
	'Student_Id' INTEGER,
	FOREIGN KEY('Exercise_Id') REFERENCES 'Exercises'('Exercise_Id'),
	FOREIGN KEY('Student_Id') REFERENCES 'Students'('Student_Id')
);

-- creating cohorts
INSERT INTO Cohorts (Cohort_Name)
VALUES("C36");

INSERT INTO Cohorts (Cohort_Name)
VALUES("C37");

INSERT INTO Cohorts (Cohort_Name)
VALUES("C38");

-- create exercises
INSERT INTO Exercises (Exercise_Name, Exercise_Language)
VALUES("Nutshell", "JavaScript");

INSERT INTO Exercises (Exercise_Name, Exercise_Language)
VALUES("Welcome to Nashville", "JavaScript");

INSERT INTO Exercises (Exercise_Name, Exercise_Language)
VALUES("Student Exercises", "Python");

INSERT INTO Exercises (Exercise_Name, Exercise_Language)
VALUES("Kennel", "React");

INSERT INTO Exercises (Exercise_Name, Exercise_Language)
VALUES("Celebrity Tribute", "HTML");

-- create instructors
INSERT INTO Instructors (First_Name, Last_Name, Slack_Handle, Specialty, Cohort_Id)
VALUES("Joe", "Shepherd", "joes", "making python funny", 1);

INSERT INTO Instructors (First_Name, Last_Name, Slack_Handle, Specialty, Cohort_Id)
VALUES("Brenda", "Long", "bjlong", "UI/UX", 3);

INSERT INTO Instructors (First_Name, Last_Name, Slack_Handle, Specialty, Cohort_Id)
VALUES("Jisie", "David", "jisie", "Star Trek trivia", 2);

-- create students
INSERT INTO Students (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES("John", "Long", "John Long", 1);

INSERT INTO Students (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES("Ryan", "Bishop", "RDB", 1);

INSERT INTO Students (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES("Trey", "Suiter", "Trey", 1);

INSERT INTO Students (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES("Holden", "Parker", "Holden", 2);

INSERT INTO Students (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES("Steve", "Young", "Stevie", 2);

INSERT INTO Students (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES("Daniel", "Green", "Danny", 3);

INSERT INTO Students (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES("Bito", "Mann", "Bito", 3);

-- create exercises to students
-- student 1
INSERT INTO Student_Exercise (Exercise_Id, Student_Id)
VALUES(1, 1);

INSERT INTO Student_Exercise (Exercise_Id, Student_Id)
VALUES(5, 1);

--student 2

INSERT INTO Student_Exercise (Exercise_Id, Student_Id)
VALUES(2, 2);

INSERT INTO Student_Exercise (Exercise_Id, Student_Id)
VALUES(4, 2);

-- student 3
INSERT INTO Student_Exercise (Exercise_Id, Student_Id)
VALUES(3, 3);

INSERT INTO Student_Exercise (Exercise_Id, Student_Id)
VALUES(1, 3);

-- student 4
INSERT INTO Student_Exercise (Exercise_Id, Student_Id)
VALUES(1, 4);

INSERT INTO Student_Exercise (Exercise_Id, Student_Id)
VALUES(2, 4);

-- student 5
INSERT INTO Student_Exercise (Exercise_Id, Student_Id)
VALUES(3, 5);

INSERT INTO Student_Exercise (Exercise_Id, Student_Id)
VALUES(1, 5);

--student 6
INSERT INTO Student_Exercise (Exercise_Id, Student_Id)
VALUES(2, 6);

INSERT INTO Student_Exercise (Exercise_Id, Student_Id)
VALUES(4, 6);

-- student 7
INSERT INTO Student_Exercise (Exercise_Id, Student_Id)
VALUES(3, 7);

INSERT INTO Student_Exercise (Exercise_Id, Student_Id)
VALUES(4, 7);
