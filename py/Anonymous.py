import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

x=input("how many players are playing? ")
x = int(x)
texts = []

for i in range(x):
    input("Press Enter to continue")
    text = input("Enter your text: ")
    texts.append(text)
    clear()

random.shuffle(texts)

input("Press Enter to start the game")
clear()

for i in range(len(texts)):
    input(f"Press Enter to show the text number {i+1}")
    print(texts[i])
    input("Press Enter to continue")
    clear()

print("end of the game")
