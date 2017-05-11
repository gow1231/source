
from tkinter import * # 여러장의 이미지를 연속으로 보여주어 애니메이션화하는 모듈
import random
import time

tk = Tk()      # 1. tk 를 인스턴스화 한다.
tk.title("Ping Pong Game")  # 2. tk 객체의 title 메소드(함수)로 게임창에 제목을 부여한다.
tk.resizable(0, 0) # 3. 게임창의 크기는 가로나 세로로 변경될수 없다라고 말하는것이다.
tk.wm_attributes("-topmost", 1) #4. 다른 모든 창들 앞에 캔버스를 가진 창이 위치할것을 tkinter 에게 알려준다.
canvas = Canvas(tk, width=400, height=500, bd=0, highlightthickness=0)
# bg=0,highlightthickness=0 은 캔버스 외곽에 둘러싼
# 외곽선이 없도록 하는것이다. (게임화면이 좀더 좋게)
#canvas.configure(background = 'black') # 캔버스 색 변경하는 방법
canvas.pack()       # 앞의 코드에서 전달된 폭과 높이는 매개변수에 따라 크기를 맞추라고 캔버스에에 말해준다.
tk.update()   # tkinter 에게 게임에서의 애니메이션을 위해 자신을 초기화하라고 알려주는것이다.

#창이 바로 꺼지는것을 막을려면 ?   mainloop() 라 불리는 애니메이션 루프를 추가해야한다.

tk.mainloop()
