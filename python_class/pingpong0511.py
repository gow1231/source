
from tkinter import *
import random
import time


class Ball:

    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        canvas.configure(background='black')
        self.canvas.move(self.id, 245, 100)
        starts = [ -1,-2,-3 , 1,2,3]
        random.shuffle(starts)

        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        #print(self.canvas_height)
        self.canvas_width = self.canvas.winfo_width()
        #print(self.canvas_width)
        self.hit_bottom = False
        self.isMiss = False
        self.canvas.bind_all('<space>', self.start)
        self.x = 0
        self.y = 0

    def start(self,evt):
        self.x = random.sample(range(-5,6),1)
        self.y = 5

    def turn_start(self,evt):
        starts = [-1, -2, -3, -4]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = starts[0]


    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        if self.hit_paddle(pos) == True:
            self.y = -3
            print('1')

    def hit_paddle(self,pos):

        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
        return False


    def winner(self, winner):
        if self.isMiss == True:
            return -1
        elif self.hit_paddle() == True:
            return 1
        else:
            return 0

    def game_over(self):
        pos = self.canvas.coords(self.id)
        if pos[1] < 400 < pos[3] and self.isMiss == False and self.y > 0:
            self.isMiss = True
            print('-1')
        elif pos[1] > 400 or pos[3] < 400:
            self.isMiss = False

class Paddle:

    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id, 200, 400)
        self.x = 0
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)

    def draw(self):
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 and self.x < 0: # 패들의 방향도 같이 써주자
            return # 함수 종료해라
        elif pos[2] >= self.canvas_width and self.x > 0:
            return # 함수 종료해라

        self.canvas.move(self.id, self.x, 0) # 이 코드의 위치는 여기!!

    def turn_left(self, evt):
        self.x = -9

    def turn_right(self, evt):
        self.x = 9

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=600, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
paddle = Paddle(canvas,'white')
ball = Ball(canvas, paddle, 'white')


while 1:
    ball.draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.015)




