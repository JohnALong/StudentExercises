class Instructor:
    def __init__(self, first_name, last_name, slack, specialty, cohort):
        self.first_name = first_name
        self.last_name = last_name
        self.slack = slack
        self.cohort = cohort
        self.specialty = specialty

    def assign_exercise(self, cohortobj, exerciseobj):
        for student in cohortobj.students:
            student.exercises.append(exerciseobj)