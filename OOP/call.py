class Callee:
    def __call__(self, *args, **kwargs):
        print('Called: ', args, kwargs)

C = Callee()
C(1, 2, 3, y=4)


class Callback:
    def __init__(self, color):
        self.color = color
    def changeColor(self):
        print('turn', self.color)

    def __call__(self):
        self.changeColor()

C = Callback('Yellow')
obj = C.changeColor
obj()