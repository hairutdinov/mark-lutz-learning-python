class SharedData:
    spam = 42


x = SharedData()
y = SharedData()

SharedData.spam = 99

print(x.spam)
print(y.spam)


class NextClass:
    def printer(self, text):
        self.message = text
        print(self.message)
x = NextClass()
x.printer('Instance call')
NextClass.printer(x, 'Class call')
print(x.message)