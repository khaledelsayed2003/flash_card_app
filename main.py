from tkinter import *
 
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

window = Tk()
window.title("Improve your Turkish vocab!")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


canvas = Canvas(width=800, height=526)
card_img = PhotoImage(file="flash_card_app/images/card_front.png")
canvas.create_image(400, 263, image= card_img)
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text="Turkish", font=(FONT_NAME, 40, "italic"))
canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="flash_card_app/images/wrong.png")
wrong_button = Button(image= wrong_img, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0, padx=100, pady=50)

right_img = PhotoImage(file="flash_card_app/images/right.png")
right_button = Button(image= right_img, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR)
right_button.grid(row=1, column=1, padx=100, pady=50)









































window.mainloop()

