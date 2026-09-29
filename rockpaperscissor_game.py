import tkinter as tk
import random


width = 500
height = 500


 
choices = ['rock', 'paper', 'scissor']
playerpoints = 0
computerpoints = 0
draws = 0


def play(player_choice):
    global playerpoints, computerpoints, draws

    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        draws += 1
        result_text = "DRAW"
    elif (player_choice == "rock" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "scissor") or \
         (player_choice == "scissor" and computer_choice == "rock"):
        computerpoints += 1
        result_text = "Computer wins!"
    else:
        playerpoints += 1
        result_text = "Player wins!"

    
    you_label.config( text=f"You chose: {player_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result_text)
    score_label.config(text=f"Player: {playerpoints}   Computer: {computerpoints}   Draws: {draws}")


def reset_game():
    global playerpoints, computerpoints, draws
    playerpoints = 0
    computerpoints = 0
    draws = 0
    you_label.config(text="You chose: -")
    computer_label.config(text="Computer chose: -")
    result_label.config(text="Make your move!")
    score_label.config(text="Player: 0   Computer: 0   Draws: 0")

def start_game():
    start_frame.place_forget()

def quit_game ():
    window.destroy()

def name():
    name = input("Enter your name : ")

 
window = tk.Tk()
window.title("Rock Paper Scissor")
window.geometry(f"{width}x{height}")
window.resizable(False , False )


title_label = tk.Label( text="Rock Paper Scissor", font=("Bell MT", 34, "bold") , highlightthickness = 0 )
title_label.pack(pady=20)

result_label = tk.Label( text="Make your move!", font=("Bell MT", 14))
result_label.pack(pady=5)

you_label = tk.Label( text="You chose: -", font=("Bell MT", 12))
you_label.pack()

computer_label = tk.Label( text="Computer chose: -", font=("Bell MT", 12))
computer_label.pack()


button_frame = tk.Frame(window)
button_frame.pack(pady=15)


rock_button = tk.Button(button_frame, text="Rock", width=8,
                         command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=8,
                          command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=5)

scissor_button = tk.Button(button_frame, text="Scissor", width=8,
                            command=lambda: play("scissor"))
scissor_button.grid(row=0, column=2, padx=5)

score_label = tk.Label(window, text="Player: 0   Computer: 0   Draws: 0", font=("BELL MT", 12))
score_label.pack(pady=10)

reset_button = tk.Button(window, text="Reset Score", command=reset_game)
reset_button.pack(pady=5)


quit_frame = tk.Button(window , text = "QUIT" , width = 24 , font= ( "BELL MT " , 12 ) , command = quit_game)
quit_frame.place( relx = 0.5 , y = 450 , anchor = "s") 

start_frame = tk.Frame(window)
start_frame.place( x = 0 , y = 0 , relwidth = 1 , relheight = 1 )

name_frame = tk.Frame(window)
start_game_button = tk.Button(start_frame, text = "START" , width = 24 ,font = ( "BEll MT" , 12),  command =  start_game)
start_game_button.place(relx=0.5, y=250, anchor="center")



window.mainloop()