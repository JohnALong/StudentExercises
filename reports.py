import sqlite3
from student import Student
from cohort import Cohort
from exercise import Exercise
from instructor import Instructor


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
                print(student, student.Cohort_Name)

    # get instructor with cohort
    def all_instructors(self):

        """Retrieve all instructors with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(
                row[1], row[2], row[3], row[5], row[6]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Instructor_Id,
                i.First_Name,
                i.Last_Name,
                i.Slack_Handle,
                i.Cohort_Id,
                c.Cohort_Name,
                i.Specialty
            from Instructors i
            join Cohorts c on i.Cohort_Id = c.Cohort_Id
            order by i.Cohort_Id
            """)

            all_instructors = db_cursor.fetchall()

            for instructor in all_instructors:
                print(instructor, instructor.Cohort_Name)

    #get all cohorts
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

    #get all exercises
    def all_exercises(self):

        """Retrieve all exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Exercise_Id,
                e.Exercise_Name,
                e.Exercise_Language
            from Exercises e
            order by e.Exercise_Id
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)

    #javascript exercises printed out
    def js_exercises(self):

        """Retrieve exercises by language"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2]
            )

            db_cursor = conn.cursor()
            language = ("JavaScript",)
            db_cursor.execute("""
            select e.Exercise_Id,
                e.Exercise_Name,
                e.Exercise_Language
            from Exercises e
            where e.Exercise_Language =?""", language
            )

            select_exercises = db_cursor.fetchall()

            for exercise in select_exercises:
                print(exercise)

    #python exercises printed out
    def python_exercises(self):

        """Retrieve exercises by language"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2]
            )

            db_cursor = conn.cursor()
            language = ("Python",)
            db_cursor.execute("""
            select e.Exercise_Id,
                e.Exercise_Name,
                e.Exercise_Language
            from Exercises e
            where e.Exercise_Language =?""", language
            )

            select_exercises = db_cursor.fetchall()

            for exercise in select_exercises:
                print(exercise)

reports = StudentExerciseReports()
reports.all_students()
reports.all_instructors()
reports.all_cohorts()
reports.all_exercises()
reports.js_exercises()
reports.python_exercises()