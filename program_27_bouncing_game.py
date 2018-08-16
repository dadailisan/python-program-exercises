#BOUNCING GAME

from tkinter import *
import random, time

tk = Tk()
tk.title("Bouncing Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

#CREATING THE CANVAS
canvas = Canvas(tk, width=500, height=400)
canvas.pack()
tk.update()

#CREATING THE BALL

class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.score = score
        self.paddle = paddle
        self.ballid = canvas.create_oval(0, 0,  15, 15, fill=color) #size & color of ball 
        self.canvas.move(self.ballid, 100, 150) #initial position ball position
        self.canvas_height = self.canvas.winfo_height() #returns the height of the canvas
        self.canvas_width = self.canvas.winfo_width() #returns the width of the canvas
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        #starts = randint(-3-3) > im trying to use random int to generate starts value
        self.x = starts[0]
        self.y = -3
        self.hit_bottom = False

    def hit_paddle(self, ballpos):
        paddle_pos = self.canvas.coords(self.paddle.paddleid)
        if ballpos[2] >= paddle_pos[0] and ballpos[0] <= paddle_pos[2]:
            if ballpos[3] >= paddle_pos[1] and ballpos[3] <= paddle_pos[3]:
                self.x += self.paddle.x
                self.score.hit()
                return True
        return False

    def drawball(self):
        self.canvas.move(self.ballid, self.x, self.y) #movement
        ballpos = self.canvas.coords(self.ballid) #store coordinates
        if ballpos[1] <= 0:
            self.y = 3
        if ballpos[3] >= self.canvas_height:
            #self.y = -3
            self.hit_bottom = True
        if ballpos[0] <= 0:
            self.x = 3
        if ballpos[2] >= self.canvas_width:
            self.x = -3
        if self.hit_paddle(ballpos) == True:
            self.y = -3


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.paddleid = canvas.create_rectangle(0, 0, 100, 10, fill=color) #size & color of paddle
        self.canvas.move(self.paddleid, 202, 330) #positiong of paddle
        self.canvas_width = self.canvas.winfo_width() #returns the width of the canvas
        self.x = 0
        self.started = False
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<Button-1>', self.start_game)

    def drawpaddle(self):
        self.canvas.move(self.paddleid, self.x, 0) #only x coordinate changes on paddle
        paddlepos = self.canvas.coords(self.paddleid) #store coordinates
        if paddlepos[0] <= 0:
            self.x = 3
        elif paddlepos[2] >= self.canvas_width:
            self.x = -3   
    def turn_left(self, event):
        self.x = -3
    def turn_right(self, event):
        self.x = 3
    def start_game(self, event):
        self.started = True


class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.scoreid = canvas.create_text(450, 10, text=self.score, fill=color)

    def hit(self):
        self.score += 100
        self.canvas.itemconfig(self.scoreid, text=self.score)

score = Score(canvas, 'blue')
paddle = Paddle(canvas, 'red')
ball = Ball(canvas, paddle, score, 'green')
game_over_text = canvas.create_text(250, 200, text='GAME OVER', state='hidden')

while True:
    if ball.hit_bottom == False and paddle.started == True:
        ball.drawball()
        paddle.drawpaddle()
    if ball.hit_bottom == True:
        time.sleep(1)
        canvas.itemconfig(game_over_text, state='normal')
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

