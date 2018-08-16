#Bouncing Game Remake

from tkinter import * #Para di mo na kailangan i-type ang tkinter. to use its functions
#sample "tkinter.Tk()" magiging "Tk()" na lang
import random, time #importing modules needed for the program

#INITIALIZING TKINTER WIDGET
tk = Tk() #This will initialize the tkinter widget.
          #Error ito pag di ka nag "from tkinter import *"

tk.title("Bounce Game!!!") #This will make title for the widget
tk.resizable(width=False, height=False) #This will make the widget window resizable or not.
                                        #Can take boolean value(True, False) or 0(False) and 1 or any value>0(True/None)

tk.wm_attributes("-topmost", True) #This will place our wkinter widget on top of all the windows


#CREATING THE CANVAS
canvas = Canvas(tk, width=500, height=400, highlightthickness=0) #Canvas is a tkinter class that takes values
                                           #widget(tk), Xview(width), YView(height)
                                            #highlightthickness=0 to ensure that there are no excess on the edges of the widget
canvas.pack() #reload and resize the widget based on the width and height
tk.update() #initialize tkinter for animation, also update the canvas

#CREATING THE BALL


class Ball:
    def __init__(self, canvas, paddle, score, color): #self is the class object and for this program it is "ball"
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.color = color
        self.ballid = canvas.create_oval(10, 10, 25, 25, fill=self.color)#creates the ball(sqaure) and color
        #for creating a polygon(create_polygon) at least 3 coordinates are needed
        self.canvas.move(self.ballid, 230, 200) #move the ball to an initial location
##        self.x = 0 #changed to starts list to randomize
##        self.y = -1 #changed to -3 since the list starts form -3 to 3
        starts = [-3, -2, -1, 1, 2, 3] #list to be used to have random angle for the ball
        random.shuffle(starts) #shuffle the list
        self.x = starts[0] #selecting the first value of list after shuffle. to be used on drawball() canvas.move
        self.y = -3 #inital value for drawball, canvas.move
        self.canvas_height = self.canvas.winfo_height() #winfo_height() function returns the height of the widget
        self.canvas_width = self.canvas.winfo_width() #winfo_width() function returns the width of the widget
        self.hit_bottom = False

    def drawball(self):
        self.canvas.move(self.ballid, self.x, self.y) #.move take 3 arguments(ID, x coor, y coor)
        ballpos = self.canvas.coords(self.ballid) #coords returns the coordinates of the item(x1, y1, x2, y2)
        #x1[index 0], y1[index 1], x2[index 2], y2[index 3]
        if ballpos[1] <= 0: #ballpos[1] initial value is y1(adding y1(self.ballid) + y(self.canvas.move))
            self.y = 3 #if ballpos[1] is equal to 0, its already at top of the widget and needs to go back DOWN
        if ballpos[3] >= self.canvas_height: #ballpos[3] initial value is y2(adding y2(self.ballid) + y(self.canvas.move))
            ##self.y = -3 #if ballpos[3] is equal to self.canvas_height(which is 400 on our program), its already at the bottom of the widget and needs to go back UP
            self.hit_bottom = True
        if ballpos[0] <= 0: #ballpos[0] intial value is x1(adding x1(self.ballid) + x(self.canvas.move))
            self.x = 3 #if ballpos[0] is equal to 0, its already at the left most of the widget
        if ballpos[2] >= self.canvas_width: #ballpos[2] inital value is x2(adding x2(self.ballid) + x(self.canvas.move))
            self.x = -3 #if ballpos[2] is equal to self.canvas_width(which is 500). its already on the right most of the widget
        if self.ball_hit_paddle(ballpos) == True:
            self.y = -3

    def ball_hit_paddle(self, ballpos):
        paddle_pos = self.canvas.coords(self.paddle.paddleid)
        if ballpos[2] >= paddle_pos[0] and ballpos[0] <= paddle_pos[2]: #from the book
            if ballpos[3] >= paddle_pos[1] and ballpos[3] <= paddle_pos[3]:
                self.x += self.paddle.x
                self.score.hit()
                return True
        return False
        

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.paddleid = canvas.create_rectangle(0, 0, 100, 10, fill=self.color) #size and location of paddle
        self.canvas.move(self.paddleid, 200, 350) #initial position of paddle
        self.x = 0
        self.canvas_width = self.canvas.winfo_width() #returns the width of the widget
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<Button-1>', self.left_click) #left click to change self.start to True that will start the game
        self.start = False #needed so that the wont start immediately, unless you left click
        

    def turn_left(self, event):
        self.x = -2
    def turn_right(self, event):
        self.x = 2
    def left_click(self, event):
        self.start = True
        self.canvas.itemconfig(left_click_text, state='hidden')
       
    def drawpaddle(self):
        self.canvas.move(self.paddleid, self.x, 0)
        paddlepos = self.canvas.coords(self.paddleid)
        if paddlepos[0] <= 0:
            self.x = 2
        if paddlepos[2] >= self.canvas_width:
            self.x = -2

class Score:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.score = 0
        self.scoreid = canvas.create_text(450, 10, text=self.score, fill=color)

    def hit(self):
        self.score += 100
        self.canvas.itemconfig(self.scoreid, text=self.score)


score = Score(canvas, color='blue')
paddle = Paddle(canvas, color='green')        
ball = Ball(canvas, paddle, score, color='blue') #when assigning a variable to a Class, you need to also pass the __init__ parameters needed
game_over_text = canvas.create_text(250, 200, text='GAME OVER', state='hidden')
left_click_text = canvas.create_text(250, 150,\
                text='Left Click to Start the Game', state='normal')
press_enter = canvas.create_text(250, 230, text='PRESS ENTER TO PLAY AGAIN.', state='hidden')

while True:
    if ball.hit_bottom == False and paddle.start == True:
        ball.drawball()
        paddle.drawpaddle()
    if ball.hit_bottom == True:
        time.sleep(1)
        canvas.itemconfig(game_over_text, state='normal')
##        canvas.itemconfig(press_enter, state='normal')
    
    #tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
