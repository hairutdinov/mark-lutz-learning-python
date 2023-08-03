class Spam:
    def doit(self, message):
        print(message)

x = Spam()
f = x.doit
print(type(f))
print(type(Spam.doit))

