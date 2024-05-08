from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMERS = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    window.after_cancel(TIMERS)
    checkmark.config(text= 'TIMER')
    canvas.itemconfig(timer_text, text='00:00')
    timer.config(text='')
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    REPS += 1
    if REPS % 8 == 0:
        count_down(long_break_seconds)
        checkmark.config(text= 'BREAK', fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_seconds)
        checkmark.config(text='BREAK', fg=PINK)
    else:
        count_down(work_sec)
        checkmark.config(text='WORK', fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global TIMERS

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f'{count_min}:{count_sec}')
    if count > 0:
        TIMERS = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if REPS % 2 == 0:
            mark = ''
            work_sessions = math.floor(REPS/2)
            for _ in range(work_sessions):
                mark += '✔'
            timer.config(text=mark)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=200, pady=224, bg=YELLOW,)



canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100,  112, image=tomato)
timer_text = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2, row=1)




timer = Label( fg=GREEN, bg= YELLOW,font= ("Arial", 50, 'bold'))
timer.grid(column=2, row=4)
timer.config(padx=20, pady=20)

checkmark = Label(text= 'Timer', fg=GREEN, bg= YELLOW,font= ("Arial", 50, 'bold'))
checkmark.grid(column=2, row=0)
checkmark.config(padx=20, pady=20)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2,)
start.config(padx=5, pady=5)


reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=3, row=2)
reset.config(padx=5, pady=5)



# fg is for color in labels
# checmark  ✔
#cange canvas to grid insteas of pack








window.mainloop()
