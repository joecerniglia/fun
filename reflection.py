class gratitude:
    def __init__(self, students, instructors, professor, assessment):
        self.students=students
        self.instructors=instructors
        self.professor=professor
        self.assessment=assessment

        self.grade=self._evaluate()

    def _evaluate(self):
        if (self.assessment==10 and self.students=='A+' and
        self.instructors=='outstanding' and
        self.professor=='legendary'):
            post='I am so very grateful for '  +\
            'the students, instructors and professor, ' +\
            'Chris Myers, who made this certificate ' +\
            'so worthwhile.'
            return post
        else:
          pass

thoughts=gratitude('A+','outstanding','legendary',10)

print(thoughts.grade)
