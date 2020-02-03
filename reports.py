import sqlite3
from student import Student
from cohort import Cohort


# completed students section
class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/jlcomp45/workspace/python/StudentExercises/studentexercises.db"

    """Methods for reports on the Student Exercises database"""

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Student_Id,
                s.First_Name,
                s.Last_Name,
                s.Slack_Handle,
                s.Cohort_Id,
                c.Cohort_Name
            from Students s
            join Cohorts c on s.Cohort_Id = c.Cohort_Id
            order by s.Cohort_Id
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)

    def all_cohorts(self):

        """Retrieve all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(
                row[1]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.Cohort_Id,
                c.Cohort_Name
            from Cohorts c
            order by c.Cohort_Id
            """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort)

reports = StudentExerciseReports()
reports.all_students()
reports.all_cohorts()