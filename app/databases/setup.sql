DROP DATABASE IF EXISTS wizlearn;
CREATE DATABASE wizlearn;
USE wizlearn;
CREATE TABLE students(
	name_of_student VARCHAR(255) NOT NULL,
    class_of_student INTEGER NOT NULL,
    section_of_student VARCHAR(1) NOT NULL,
    admission_no INTEGER NOT NULL PRIMARY KEY,
    elective_club VARCHAR(255),
    elective_vpa VARCHAR(255),
    marks NVARCHAR(4000)
);
ALTER TABLE students
    ADD CONSTRAINT `[marks record should be formatted as JSON]`
                   CHECK (ISJSON(value)=1);

CREATE TABLE teachers(
	name_of_teacher VARCHAR(255) NOT NULL,
    class_teacher VARCHAR(5),
    classes_with_subject NVARCHAR(4000),
    teacher_id INTEGER NOT NULL PRIMARY KEY
);
ALTER TABLE teachers
	ADD CONSTRAINT `[classes_with_subject should be formatted as JSON]`
					CHECK (ISJSON(value)=1);
                    
CREATE TABLE admins(
	id INTEGER NOT NULL PRIMARY KEY,
    name_of_admin VARCHAR(255) NOT NULL,
    level_of_access INTEGER NOT NULL
);