BACKGROUND_COLOR = "#B1DDC6"


import random
import tkinter
import pandas
I={}
def right():
    global I,flip_timer
    window.after_cancel(flip_timer)
    I=random.choice(x)
    canvas_front.itemconfig(card_word,text=I['French'],fill="black")
    canvas_front.itemconfig(card_title,text="French",fill="black")
    canvas_front.itemconfig(card_background,image=old_image)
    flip_timer=window.after(3000,flip_card)
    
def flip_card():
    global I
    I=random.choice(x)
    canvas_front.itemconfig(card_background,image=new_image)
    canvas_front.itemconfig(card_word,text=I["English"],fill="white")
    canvas_front.itemconfig(card_title,text="English",fill="white")

def is_known():
    x.remove(I)
    data=pandas.DataFrame(x)
    data.to_csv(file="/home/sameeranati/flashy/data/words_to_learn.csv",index=False)
    right()
    


# --------------------------------------------------UI SETUP-------------------------------------------------------------
window=tkinter.Tk()
window.title("Flashy")
window.minsize(width=900,height=500)
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,flip_card)

# ------------------------------------------------FRONT CARD-----------------------------------------
canvas_front=tkinter.Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
old_image=tkinter.PhotoImage(file="/home/sameeranati/flashy/images/card_front.png")
new_image=tkinter.PhotoImage(file="/home/sameeranati/flashy/images/card_back.png")
card_background=canvas_front.create_image(400,270,image=old_image)
card_title=canvas_front.create_text(400,150,text="",font=('Ariel',40,"italic"))
card_word=canvas_front.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas_front.grid(row=0,column=0,columnspan=2)

# -------------------------------------------RIGHT BUTTON IMAGE-------------------------------------------------
canvas_right=tkinter.Canvas(bg=BACKGROUND_COLOR,highlightthickness=0)
tt=tkinter.PhotoImage(file="/home/sameeranati/flashy/images/right.png")
right_image=canvas_right.create_image(100,100,image=tt)

# def right():
#     I=random.choice(x)
#     canvas_front.itemconfig(card_word,text=I["French"])
#     canvas_front.itemconfig(card_title,text="French")
#     canvas_front.itemconfig(400,270,image=new_image)
#     canvas_front.itemconfig(card_word,text=I["English"])
#     canvas_front.itemconfig(card_title,text="English",fill="white")


right_button=tkinter.Button(image=tt,borderwidth=0,bg=BACKGROUND_COLOR,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=0)
# ----------------------------------------------WRONG BUTTON-------------------------------------------
canvas_wrong=tkinter.Canvas(bg=BACKGROUND_COLOR,highlightthickness=0)
ttt=tkinter.PhotoImage(file="/home/sameeranati/flashy/images/wrong.png")
wrong_image=canvas_right.create_image(100,100,image=ttt)

wrong_button=tkinter.Button(image=ttt,command=right,borderwidth=0,bg=BACKGROUND_COLOR,highlightthickness=0)
wrong_button.grid(row=1,column=1)

global x

try:
    with open("/home/sameeranati/flashy/data/words_to_learn.csv") as file:
        data=pandas.read_csv(file)
    
except FileNotFoundError:
    with open("/home/sameeranati/flashy/data/french_words.csv",'w') as file:

        data=pandas.read_csv(file)
    
else:     
    x=data.to_dict(orient="records")
    right()
    window.mainloop()