import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

x=input("how many players are playing? ")
x = int(x)
players = {}

for i in range(x):
    input("Press Enter to continue")
    name = input(f"Enter player{i+1} name: ")
    text = input("Enter your text: ")
    players[name] = text
    clear()

texts= list(players.values())
random.shuffle(texts)

input("Press Enter to start the game")
clear()

for i in range(len(texts)):
    input(f"Press Enter to show the text (player{i+1})3")
    print(texts[i])
    input("Press Enter to continue")
    clear()

input("do you want to see truth? press Enter")
clear()

print(players)



    
