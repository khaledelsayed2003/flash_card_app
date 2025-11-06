# 🇹🇷 Turkish Flash Card App (Tkinter + CSV)

A simple Python GUI app that helps you learn Turkish vocabulary using flash cards (TR → EN) with progress saving and sound effects.

---


## 🌿 Features

- Random Turkish flash cards

- Automatic flip to English after delay

- ✅ “Correct answer” sound effect

- 🎉 “Congrats” sound when all words are learned

- Saves progress into words_to_learn.csv

- Clean & smooth Tkinter UI

--- 

## 🧩 Project Structure
```bash
flash_card_app/
├─ data/
│  ├─ turkish_words.csv
│  └─ words_to_learn.csv
│
├─ images/
│  ├─ card_front.png
│  ├─ card_back.png
│  ├─ congrats_message.png
│  ├─ en_word.png
│  ├─ right_button_clicked.png
│  ├─ right.png
│  ├─ tr_word.png
│  └─ wrong.png
│
├─ sounds/
│  ├─ congrats.mp3
│  └─ correct_button_clicked.mp3
│
├─ main.py             
├─ README.md     

--- 


##⚙️ Setup & Usage
####📦 Requirements
- Python 3.9+
- Install libraries:
     - pip install pandas playsound



--- 


## 📚 Learn Words Flow

1- Turkish word appears first

2- After a short timer → flips to English

3- If you know the word → click ✅

4- Word is removed & saved in words_to_learn.csv

5- 🎓 Ending

6- When no words remain → app displays “Great Job!” + plays a success sound
--- 

## 👨‍💻 Author

Khaled Elsayed

- Built using Python + Tkinter

- added sound feedback to improve memory learning

## 📄 License

- This project is for educational and personal use.

## © 2025 – Khaled Elsayed.