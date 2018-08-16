#classes and objects

#classes
class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalk(Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print('Breathing...')
    def move(self):
        print('Moving...')
    def eat_food(self):
        print('Eating food...')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('Feeding young...')

class Giraffes(Mammals):
    #def __init__(self, spots):
    #    self.giraffes_spots = spots
    def find_food(self):
        self.move()
        print('I\'ve found food!')
        self.eat_food()
    def eat_leaves_from_trees(self):
        self.eat_food()
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()
    def left_foot_forward(self):
        print('Left foot forward...')
    def left_foot_backward(self):
        print('Left foot backward...')
    def right_foot_forward(self):
        print('Right foot forward...')
    def right_foot_backward(self):
        print('Right foot backward...')
    def dance(self):
        self.left_foot_forward()
        self.left_foot_backward()
        self.right_foot_forward()
        self.right_foot_backward()
        self.left_foot_backward()
        self.right_foot_backward()
        self.right_foot_forward()
        self.left_foot_forward()
#objects

reginald = Giraffes()
harold = Giraffes()
