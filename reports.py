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

    def exercises_by_instructors(self):

        """Retrieve all exercises and what instructor assigned them"""

        with sqlite3.connect(self.db_path) as conn:

            db_cursor = conn.cursor()

            db_cursor.execute(""" SELECT
                e.Exercise_Id Exercise_Id,
                e.Exercise_Name,
                i.Instructor_Id Instructor_Id,
                i.First_Name,
                i.Last_Name
                FROM Exercises e 
                JOIN Student_Exercise se ON se.Exercise_Id = e.Exercise_Id
                JOIN Instructors i ON i.Instructor_Id = se.Instructor_Id;
            """)

            all_exercises_by_instructors = db_cursor.fetchall()

            instructors = dict()

            for exercise_instructor in all_exercises_by_instructors:
                exercise_id = exercise_instructor[0]
                exercise_name = exercise_instructor[1]
                instructor_name = f'{exercise_instructor[3]} {exercise_instructor[4]}'

                if instructor_name not in instructors:
                    instructors[instructor_name] = [exercise_name]
                else:
                    instructors[instructor_name].append(exercise_name)

            for instructor_name, exercises in instructors.items():
                print(instructor_name)
                for exercise in exercises:
                    print(f'\t* {exercise}')

    def exercises_with_students(self):
        """Retrieve all exercises and the students working on each one"""

        with sqlite3.connect(self.db_path) as conn:

            db_cursor = conn.cursor()

            db_cursor.execute("""select
                e.Exercise_Id Exercise_Id,
                e.Exercise_Name,
                s.Student_Id Student_Id,
                s.First_Name,
                s.Last_Name
                FROM Exercises e 
                JOIN Student_Exercise se on se.Exercise_Id = e.Exercise_Id
                JOIN Students s on s.Student_Id = se.Student_Id;
             """)

            all_exercises_with_students = db_cursor.fetchall()

            # takes list of tuples and convert to dictionary to remove duplicates and create nested info for usability
            exercises = dict()

            for exercise_student in all_exercises_with_students:
                exercise_id = exercise_student[0]
                exercise_name = exercise_student[1]
                student_id = exercise_student[2]
                student_name = f'{exercise_student[3]} {exercise_student[4]}'

                if exercise_name not in exercises:
                    #1st square bracket is holding variable and denoting dictionary - 2nd bracket is denoting list
                    # exercises[exercise_name] is adding a new key/value pair to the exercises dictionary, where exercise_name is the variable containing the key value which is the string
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)

            # print students assigned to exercise without repeating exercise
            for exercise_name, students in exercises.items():
                print(f'{exercise_name} is being worked on by')
                for student in students:
                    print(f'\t* {student}')

            students = dict()

            for student_exercise in all_exercises_with_students:
                exercise_id = student_exercise[0],
                exercise_name = student_exercise[1],
                student_id = student_exercise[2],
                student_name = f'{student_exercise[3]} {student_exercise[4]}'

                if student_name not in students:
                    students[student_name] = [exercise_name]
                else:
                    students[student_name].append(exercise_name)

            for student_name, exercises in students.items():
                print(student_name)
                for exercise in exercises:
                    print(f'\t* {exercise[0]}')

    # list exercises assinged to and by whom
    def exercises_students_instructors(self):
        """Retrieve all exercises and the students working on each one and who assigned it"""

        with sqlite3.connect(self.db_path) as conn:

            db_cursor = conn.cursor()

            db_cursor.execute("""SELECT
                e.Exercise_Id Exercise_Id,
                e.Exercise_Name,
                i.Instructor_Id Instructor_Id,
                i.First_Name,
                i.Last_Name,
                s.Student_Id Student_Id,
                s.First_Name,
                s.Last_Name
                FROM Exercises e 
                JOIN Student_Exercise se ON se.Exercise_Id = e.Exercise_Id
                JOIN Instructors i ON i.Instructor_Id = se.Instructor_Id
                JOIN Students s ON se.Student_Id = s.Student_Id;
             """)

            all_exercises_students_instructors = db_cursor.fetchall()

            # takes list of tuples and convert to dictionary to remove duplicates and create nested info for usability
            exercises = {}
            instructors = {}
            students = {}

            for exercise_student in all_exercises_students_instructors:
                exercise_id = exercise_student[0]
                exercise_name = exercise_student[1]
                instructor_id = exercise_student[2]
                instructor_name = f'{exercise_student[3]} {exercise_student[4]}'
                student_id = exercise_student[5]
                student_name = f'{exercise_student[6]} {exercise_student[7]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = instructors, students

            for exercise_student in all_exercises_students_instructors:
                exercise_id = exercise_student[0]
                exercise_name = exercise_student[1]
                instructor_id = exercise_student[2]
                instructor_name = f'{exercise_student[3]} {exercise_student[4]}'
                student_id = exercise_student[5]
                student_name = f'{exercise_student[6]} {exercise_student[7]}'

                exercises[exercise_name]:instructors.append(instructor_name)
                exercises[exercise_name]:students.append(student_name)
                print(exercises)

            for exercise_name, students in exercises.items():
                print(f'{exercise_name} is being worked on by')
                for student in students:
                    print(f'\t* {student}')



reports = StudentExerciseReports()
# reports.all_students()
# reports.all_instructors()
# reports.all_cohorts()
# reports.all_exercises()
# reports.js_exercises()
# reports.python_exercises()
# reports.exercises_with_students()
# reports.exercises_by_instructors()
reports.exercises_students_instructors()

