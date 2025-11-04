from tkinter import *
import pandas as pd
from random import choice, randint

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
random_word_row = {}
# Create a new flash card(tr)
def generate_tr_word():   
    global random_word_row
    with open("flash_card_app/data/turkish_words.csv") as file:
        whole_words = pd.read_csv(file)
        whole_words_dic = whole_words.to_dict(orient="records" )
        random_word_row = choice(whole_words_dic)
        random_word_tr = random_word_row["Turkish"]
        canvas.itemconfig(title_text, text= "Turkish", fill= "#020203")
        canvas.itemconfig(word_text, text= random_word_tr, fill= "#020203")
        canvas.itemconfig(card_img, image= card_img_tr)
        # flip the card to the English version after 3 seconds.
        window.after(3000, flip_card)

# flip the card(en)
def flip_card():
    canvas.itemconfig(card_img, image= card_img_en)
    canvas.itemconfig(title_text, text= "English", fill= "#f7f9fa")
    canvas.itemconfig(word_text, text= random_word_row["English"], fill= "#f7f9fa")

     
# Create the UI
window = Tk()
window.title("Improve your Turkish vocab!")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


canvas = Canvas(width=800, height=526)
card_img_tr = PhotoImage(file="flash_card_app/images/card_front.png")
card_img_en = PhotoImage(file="flash_card_app/images/card_back.png")
card_img = canvas.create_image(400, 263, image= card_img_tr)
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
title_text = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="flash_card_app/images/wrong.png")
wrong_button = Button(image= wrong_img, command= generate_tr_word, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0, padx=100, pady=50)

right_img = PhotoImage(file="flash_card_app/images/right.png")
right_button = Button(image= right_img, command= generate_tr_word, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR)
right_button.grid(row=1, column=1, padx=100, pady=50)

generate_tr_word()


























window.mainloop()





