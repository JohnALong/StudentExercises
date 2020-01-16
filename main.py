from exercise import Exercise
from student import Student
from instructor import Instructor
from cohort import Cohort

# creating exercises
journal = Exercise("Daily Journal", "JavaScript")
nutshell = Exercise("Nutshell", "JavaScript")
cash_coins = Exercise("Cash to Coins", "Python")
kennel = Exercise("Kennel", "React")

# creating Cohorts
C36 = Cohort("C36")
E9 = Cohort("E9")
C37 = Cohort("C37")

# creating students
John = Student("John", "Long", "John Long", C36.name)
Holden = Student("Holden", "Parker", "Holden Parker", C37.name)
Anonymous = Student("Mister", "Anonymous", "This Anon Works", E9.name)
Jeremiah = Student("Jeremiah", "Bell", "Jeremiah Bell", C36.name)

#creating instructors
Joe = Instructor("Joe", "Shepherd", "Joe Shepherd", "Making Python Fun!", C36.name)
Brenda = Instructor("Brenda", "Long", "Brenda Long", "Dancing to funny videos", E9.name)
Steve = Instructor("Steve", "Brownlee", "Steve Brownlee", "Blogging", C37.name)

C36.add_instructor(Joe)
C37.add_instructor(Steve)
E9.add_instructor(Brenda)

C36.add_student(John)
C36.add_student(Jeremiah)
C37.add_student(Holden)
E9.add_student(Anonymous)

E9.show_students()
C36.show_students()
Joe.assign_exercise(C36, kennel)
Joe.assign_exercise(C36, journal)
Brenda.assign_exercise(E9, cash_coins)
Brenda.assign_exercise(E9, kennel)
Steve.assign_exercise(C37, nutshell)
Steve.assign_exercise(C37, journal)

John.student_info()
Jeremiah.student_info()
Holden.student_info()








