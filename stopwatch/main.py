from tkinter import *
import math
TIMER_TEXT_COLOUR = "#f9b73b"
SILVER = "#afaeac"
FONT = "Bebas Neue"
STATE = FALSE
TIME_REMAINS = None
TIMER = None

# ------------------------- RESET MECHANISM --------------------------- #


def reset_timer():
    windows.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00:00")

# ---------------------- PAUSE_PLAY MECHANISM ------------------------- #


def pause_play_timer():
    global STATE
    if pause_play["text"] == "▶":
        pause_play.config(text="⏸")
        STATE = True
        countdown(TIME_REMAINS)
    else:
        pause_play.config(text="▶")
        STATE = False


# ------------------------ TIMER MECHANISM ---------------------------- #


def start_timer():
    global STATE
    STATE = True
    t_hour = int(hour_spin.get()) * 3600
    t_min = int(min_spin.get()) * 60
    t_sec = int(sec_spin.get())
    time = t_hour + t_min + t_sec
    if pause_play["text"] == "▶":
        pause_play.config(text="⏸")
    countdown(time)
# ---------------------- COUNTDOWN MECHANISM -------------------------- #


def countdown(count):
    count_hour = math.floor(count / 3600)
    count_min = math.floor((count - (count_hour * 3600))/60)
    count_sec = count % 60

    if count_hour < 10:
        standard_count_hour = f"0{count_hour}"
    else:
        standard_count_hour = count_hour
    if count_min < 10:
        standard_count_min = f"0{count_min}"
    else:
        standard_count_min = count_min
    if count_sec < 10:
        standard_count_sec = f"0{count_sec}"
    else:
        standard_count_sec = count_sec

    global STATE
    if STATE == True:
        canvas.itemconfig(timer_text, text=f"{standard_count_hour}:{standard_count_min}:{standard_count_sec}")
        if count > 0:
            global TIMER
            TIMER = windows.after(1000, countdown, count - 1)
            global TIME_REMAINS
            TIME_REMAINS = (count_hour * 3600) + (count_min * 60) + count_sec


# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Stopwatch")
windows.config(padx=20, pady=20, bg=TIMER_TEXT_COLOUR)

title = Label(text="STOPWATCH", font=(FONT, 40, "normal"), bg=TIMER_TEXT_COLOUR)
title.grid(column=1, row=0)

canvas = Canvas(width=300, height=300, highlightthickness=0)
stopwatch_img = PhotoImage(file="timer_plane.png")
canvas.create_image(150, 150, image=stopwatch_img)
timer_text = canvas.create_text(150, 150, text="00:00:00", fill=TIMER_TEXT_COLOUR, font=(FONT, 35, "normal"))
canvas.grid(column=1, row=1)

min_spin = Spinbox(from_=0, to=59, width=5, bg=SILVER)
min_spin.grid(column=1, row=3)

sec_spin = Spinbox(from_=0, to=59, width=5, bg=SILVER)
sec_spin.grid(column=1, row=4)

hour_spin = Spinbox(from_=0, to=60, width=5, bg=SILVER)
hour_spin.grid(column=1, row=2)

start_pause_play = Button(text="Start", font=("Courier", 20, "bold"), command=start_timer)
start_pause_play.grid(column=1, row=6)

pause_play = Button(text="⏸", fg=TIMER_TEXT_COLOUR, command=pause_play_timer, font=20, bg="Black",
                    highlightcolor="Black")
pause_play.grid(column=2, row=5)

restart = Button(text="🔁", command=reset_timer, fg=TIMER_TEXT_COLOUR, font=20, highlightcolor="Black", bg="Black")
restart.grid(column=0, row=5)

mainloop()
