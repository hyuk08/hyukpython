import turtle # 그래픽 모듈
import math
import random
wn = turtle.Screen() # 스크린 객체 생성
turtle.tracer(8,0)
alex = turtle.Turtle() # 객체 생성(거북이 생성)
alex.hideturtle() # 아이콘 숨기기
r=200
for i in range(5000):
    u=random.random()
    d = r*(u**0.5)
    theta = random.random()*360
    x = d * math.cos(math.radians(theta))
    y = d * math.sin(math.radians(theta))
    alex.penup()
    alex.setposition(x,y)
    alex.dot()
turtle.update()
wn.mainloop()