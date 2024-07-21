from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1,1)

t_font = ("Boulder", 69, 'bold')
bg_color = "#21130d"
t_color = "#eeeee4"
border_width = 21

label = Label(app_window, font=t_font, bg=bg_color, fg=t_color, bd= border_width)

label.grid(row=0, column=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()