import turtle



class Pitchfork():
    def one(self):
        self = turtle.Pen()
        self.forward(50)
        self.left(90)
        self.forward(30)
        self.right(90)
        self.forward(50)

    def two(self):
        self = turtle.Pen()
        self.forward(70)
        self.left(90)
        self.forward(10)
        self.right(90)
        self.forward(30)

    def three(self):
        self = turtle.Pen()
        self.forward(70)
        self.right(90)
        self.forward(10)
        self.left(90)
        self.forward(30)

    def four(self):
        self = turtle.Pen()
        self.forward(50)
        self.right(90)
        self.forward(30)
        self.left(90)
        self.forward(50)

    def test(self):
        print('testing...')

one = Pitchfork()
two = Pitchfork()
three = Pitchfork()
four = Pitchfork()
