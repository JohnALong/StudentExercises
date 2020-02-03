class Cohort:
    def __init__(self, name,):
        self.Cohort_Name = name
        self.students = list()
        self.instructors = list()

    def __repr__(self):
        return f'{self.Cohort_Name} is full'

    def add_student(self, student):
        self.students.append(student)

    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def show_students(self):
        for student in self.students:
            print(student.slack)


