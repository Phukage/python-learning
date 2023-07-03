import tkinter as ui 
import time
import math

window = ui.Tk()
window.title('My Clock')
window.geometry("400x400")

canvas = ui.Canvas(window, width=400, height=400, bg="white")
canvas.pack(expand=True, fill='both')

bg = ui.PhotoImage(file='clock.png')
canvas.create_image(200, 200, image=bg)


def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))
    seconds_x = second_hand_len * math.sin(math.radians(seconds * 6)) + center_x
    seconds_y = -1 * second_hand_len * math.cos(math.radians(seconds*6)) + center_x
    canvas.coords(second_hand, center_x, center_y, seconds_x, seconds_y)
    
    minutes_x = minute_hand_len * math.sin(math.radians(minutes * 6)) + center_x
    minutes_y = -1 * minute_hand_len * math.cos(math.radians(minutes*6)) + center_x
    canvas.coords(minute_hand, center_x, center_y, minutes_x, minutes_y)
    
    hours_x = minute_hand_len * math.sin(math.radians(hours * 30)) + center_x
    hours_y = -1 * minute_hand_len * math.cos(math.radians(hours*30)) + center_x
    canvas.coords(hour_hand, center_x, center_y, hours_x, hours_y)
    
    window.after(1000, update_clock)

#Create cloc hand
center_x = 200
center_y = 200
second_hand_len = 95
minute_hand_len = 80
hour_hand_len = 60

#Drawing clock hands
second_hand = canvas.create_line(200,200, 200 + second_hand_len, 200 + second_hand_len, width=1.5, fill='red')
minute_hand = canvas.create_line(200,200, 200 + minute_hand_len, 200 + minute_hand_len, width=2, fill='black')
hour_hand = canvas.create_line(200,200, 200 + hour_hand_len, 200 + hour_hand_len, width=4, fill='black')


update_clock()


window.mainloop()