logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
print("Welcome to black jack!")
import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
me = []
computer = []

card_one = random.choice(cards)
card_two = random.choice(cards)
card_three = random.choice(cards)
card_four = random.choice(cards)

me.append(card_one)
me.append(card_two)
computer.append(card_three)
computer.append(card_four)

def addCard():
    add_card = sum(me)
    return add_card

def addComputer():
    add_computer = sum(computer)
    return add_computer

print(f"Your cards are {me}, current score: {addCard()}")
computer_first = computer[0]
print(f"Computer's first card: {computer_first}")

def compare():
    while addComputer() < 17 or addCard() < 17:
        if addComputer() < 17:
            computer.append(random.choice(cards))
        if addCard() < 17:
            me.append(random.choice(cards))

    if (addCard() < 21 and addComputer() >= 21) or (addCard() and addComputer() < 21) and (addCard() > addComputer()):
        print(f"Your final cards are {me}, current score: {addCard()}")
        print(f"Computer's final cards are: {computer}, current score: {addComputer()}")
        print("You win")
    elif addCard() == addComputer():
        print(f"Your final cards are {me}, current score: {addCard()}")
        print(f"Computer's final cards are: {computer}, current score: {addComputer()}")
        print("You draw")
    elif (addCard() >= 21 and addComputer() < 21) or ((addCard() and addComputer() < 21) and (addCard() < addComputer())):
        print(f"Your final cards are {me}, current score: {addCard()}")
        print(f"Computer's final cards are: {computer}, current score: {addComputer()}")
        print("Computer wins")
    elif (addCard() >= 21 and addComputer() >= 21):
        print("You both lose! Try again!")

def another1():
    another = input("Type 'y' to draw another card and 'n' to pass: ")
    if another == "y": 
        me.append(random.choice(cards))
        computer.append(random.choice(cards))
        print(f"Your final cards are {me}, current score: {addCard()}")
        print(f"Computer's final cards are: {computer}, current score: {addComputer()}")
        if (addCard() >= 21 and addComputer() < 21):
            print("You lose!") 
        if (addCard() < 21 and addComputer() >= 21):
            print("You win!")
        if (addCard() >= 21 and addComputer() >= 21):
            print("You both lose! Try again!")
        if (addCard() < 21 and addComputer() < 21):
            another1()
    else:
        compare()

def draw_another():
    another1()
    

draw_another()
