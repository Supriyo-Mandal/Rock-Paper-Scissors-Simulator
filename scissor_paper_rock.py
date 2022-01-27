from tkinter import *
from PIL import Image, ImageTk
from random import randint
# Main Window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")

# Picture
rock_img = ImageTk.PhotoImage(Image.open("rock-user.jpeg"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.jpeg"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor-user.jpeg"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.jpeg"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.jpeg"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor.jpeg"))

# Insert Picture
user_label = Label(root, image=scissor_img, bg="#9b59b6")
comp_label = Label(root, image=scissor_img_comp, bg="#9b59b6")
user_label.grid(row=1, column=0)
comp_label.grid(row=1, column=4)

# Scores
playerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
playerScore.grid(row=1, column=1)
computerScore.grid(row=1, column=3)

# Indicators
user_indicator = Label(root, font=50, text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER",
                       bg="#9b59b6", fg="white")
comp_indicator.grid(row=0, column=3)
user_indicator.grid(row=0, column=1)

# Messages
msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)

# Update Message
def updateMessage(x):
    msg['text'] = x

# Update User Score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# Update Computer Score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

# Check Winner
def checkWin(player,computer):
    if player == computer:
        updateMessage("Its a Tie !!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You Loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You Loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateCompScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You Loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    else:
        pass


choices = ["rock", "paper", "scissor"]

def updateChoice(x):

    # For Computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=rock_img_comp)
    
    # For User
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkWin(x,compChoice)

# Buttons
rock = Button(root, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="white", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor")).grid(row=2, column=3)

root.mainloop()
