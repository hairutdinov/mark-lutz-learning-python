from first_class import FirstClass


class SecondClass(FirstClass):
    def display(self):
        print(f'Current value = {self.data}')
