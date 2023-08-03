from second_class import SecondClass


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return f'[ThirdClass: {self.data}]'

    def mul(self, reps):
        self.data *= reps

