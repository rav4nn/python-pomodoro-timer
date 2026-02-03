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
reps = 0
timer = None



# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
    check_marks_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global timer_label
    reps+=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps%8==0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 20))
    elif reps%2==0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50))
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec ==0 or count_sec<10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count>0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checks = ""
        for _ in range(math.floor(reps/2)):
            checks += "✔"
        check_marks_label.config(text=checks)

# ---------------------------- UI SETUP ------------------------------- #

# create window with title and size
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)
#window.minsize(width=500, height=500)


# create canvas widget
canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image = tomato_img)
# assigning a variable timer_text to the time shown
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


#create timer label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(row=0, column=1)

#create start button
start_button = Button(text="Start", highlightthickness=0, command = start_timer)
# calling count_down function through start_timer on button press
start_button.grid(row=0, column=2)
start_button.grid(row=2, column=0)

#create reset button
reset_button = Button(text="Reset", highlightthickness=0, command = reset_timer)
reset_button.grid(row=2, column=2)

#create check marks but without a check mark for now
check_marks_label = Label(bg=YELLOW, highlightthickness=0)
check_marks_label.grid(row=3, column=1)

window.mainloop()