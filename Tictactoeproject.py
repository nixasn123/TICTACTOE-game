# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.


from tkinter import *
import time
from tkinter import *
import random

def next_turn(row, column):
      global player
      if buttons[row][column]['text'] == "" and decide_winner() is False:
         if player == players[0]:
            buttons[row][column]['text'] = player
            if decide_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif decide_winner() is True:
                label.config(text=(players[0]+" wins"))
            elif decide_winner() == "Tie":
                label.config(text="Tie!")

         else:
          buttons[row][column]['text'] = player

          if decide_winner() is False:
                  player = players[0]
                  label.config(text=(players[0] + " turn"))

          elif decide_winner() is True:
                   label.config(text=(players[1] + " wins"))
          elif decide_winner() == "Tie":
                  label.config(text="Tie!")


def decide_winner():
       for row in range(3):
           if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
               return True
       for column in range(3):
           if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
               return True
           if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
               return True

           elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
               return True

           elif empty_spaces() is False:

            for row in range(3):
                for column in range(3):

                  return "Tie"

           else:
               return False

def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player

    player = random.choice(players)

    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="")


window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " turn", font=('Helvetica',40))
label.pack(side="top")

reset_button = Button(text="restart", font=('Helvetica',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)
window.mainloop()





