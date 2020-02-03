from nss_person import NSSPerson

class Student(NSSPerson):
    def __init__(self, first_name, last_name, slack, cohort):
        super().__init__(first_name, last_name, slack, cohort)
        self.exercises = list()

    def __repr__(self):
        return f'{self.First_Name} {self.Last_Name} is in {self.Cohort_Name}'

    def student_info(self):
        for exercise in self.exercises:
            print(exercise.name)
            





