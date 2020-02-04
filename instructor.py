from nss_person import NSSPerson

class Instructor(NSSPerson):
    def __init__(self, first_name, last_name, slack, cohort, specialty):
        super().__init__(first_name, last_name, slack, cohort)
        self.specialty = specialty

    def assign_exercise(self, cohortobj, exerciseobj):
        for student in cohortobj.students:
            student.exercises.append(exerciseobj)

    def __repr__(self):
        return f'{self.First_Name} {self.Last_Name} is teaching'