from tkinter import *
import math
import time

tk = Tk()
canvas = Canvas(tk, width=170, height=170)
canvas.pack()

# creat pointer
def pointer(radius, length_width, rad, color):
    x = x_center + radius * math.sin(rad)
    y = y_center - radius * math.cos(rad)
    i = canvas.create_line(x_center, y_center, x, y, width=length_width,fill=color)
    List.append(i)


# draw a circle 
canvas.create_oval(10, 10, 160, 160)


x_center, y_center, r = 85, 85, 60

# 1~12 number
for i in range(1, 13):
    x = x_center + r*math.sin(2*math.pi*i/12)
    y = y_center - r*math.cos(2*math.pi*i/12)
    canvas.create_text(x,y,text=i)


# draw middle decorate
canvas.create_oval(x_center-3, y_center-3, x_center+3, y_center+3)

# creat scal
for i in range(1, 61):
    x = x_center + (r+15)*math.sin(2*math.pi*i/60)
    y = y_center - (r+15)*math.cos(2*math.pi*i/60)
    x2 = x_center + (r+8)*math.sin(2*math.pi*i/60)
    y2 = y_center - (r+8)*math.cos(2*math.pi*i/60)
    if i % 5 == 0:
        canvas.create_line(x, y, x2, y2, width=2)
    else:
        canvas.create_line(x, y, x2, y2, width=1)

List = []


while True:
    tm = time.localtime()
    tm_hour = 0
    # change to twelve hours
    if tm.tm_hour <= 12:
        tm_hour = tm.tm_hour
    else:
        tm_hour = tm.tm_hour - 12
        rad_h = 2*math.pi*(tm_hour+tm.tm_min/60)/12      # hour hand
        rad_m = 2*math.pi*(tm.tm_min+tm.tm_sec/60)/60    # minute hand
        rad_s = 2*math.pi*tm.tm_sec/60                   # second hand

        pointer(25, 3, rad_h, 'black')
        pointer(50, 2, rad_m, 'black')
        pointer(70, 1, rad_s, 'orange')
        tk.update()
        for item in List:
            canvas.delete(item)

