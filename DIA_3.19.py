
# for i in range(4):
#     t.forward(100)
#     t.right(90)
# for i in range(4):
#     t.left(90)
#     t.forward(100)
# for i in range(4):
#     t.right(90)
#     t.forward(100)
# for i in range(3):
#     t.forward(100)
#     t.left(90)
# t.right(90)
# t.circle(100)
# t.right(90)
# t.forward(200)
# t.right(120)
# for i in range(5):
#     t.forward(100)
#     t.right(72)
import turtle
import turtle as t
import time

t = turtle.Turtle()
t.shape("turtle")
def draw_polygon(n, length):
    angle = 360 / n
    for i in range(n):
        t.forward(length)
        t.right(angle)
t.up()
t.left(180)
t.forward(300)
t.down()
n = 60
t.speed('fastest')      
for i in range(n):
    t.circle(120)       
    t.right(360 / n)
t.up()
t.left(120)
t.forward(90)
t.down()
t.right(150)

for i in range(100):
    t.right(3.6)
    for j in range(2):
        t.forward(80)
        t.right(60)
        t.forward(80)
        t.right(120)
# second
t.up()
t.left(210)
t.forward(500)
t.down()

n = 60 
for i in range(n):
    t.circle(120)       
    t.right(360 / n)

t.up()
t.right(50)
t.forward(90)
t.down()

for i in range(100):
    t.right(3.6)
    for j in range(2):
        t.forward(80)
        t.right(60)
        t.forward(80)
        t.right(120)

for i in range(1,226): 
    t.fd (100+i*5)
    t.lt(119)

# for i in range(588):    # 300번 반복
#     t.forward(i)        # i만큼 앞으로 이동. 반복할 때마다 선이 길어짐
#     t.right(91)

# for i in range(100):
#     draw_polygon(i+2, 100)

turtle.done()