from nss_person import NSSPerson

class Student(NSSPerson):
    def __init__(self, first_name, last_name, slack, cohort):
        super().__init__(first_name, last_name, slack, cohort)
        self.exercises = list()

    def student_info(self):
        for exercise in self.exercises:
            print(exercise.name)





