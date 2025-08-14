print("Welcome to Treasure Island!\nYour mission is to find the treasure")
decision = input("You are at a crossroad. Which direction do you want to go? Left or right? ")
if decision == "Left" or decision == "left":
    todo = input("You come to a lake. There is an island at the middle of that lake. Type 'wait' to wait for a boat or 'swim' to swim across. ")
    if todo == "Wait" or todo == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One of those doors contain the treasure. Which door do you choose? Red, Blue or Yellow? ")
        if door == "Red" or door == "red":
            print("You are burnt by fire! Game over!")
        elif door == "Blue" or door == "blue":
            print("You are eaten by beasts! Game over!")
        elif door == "Yellow" or door == "yellow":
            print("You winnn! Congratulations! You have found the long-lost treasure!")
        else:
            print("Game over.")
    else: 
        print("You are attacked by trout. Game over!")
else:
    print("You fall into a hole and die. Game over!")