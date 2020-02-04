class Exercise:
    def __init__(self, name, language):
        self.Exercise_Name = name
        self.Exercise_Language = language

    def __repr__(self):
        return f'{self.Exercise_Name} is done in the language of {self.Exercise_Language}'