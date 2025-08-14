print("Welcome to Virtual Coin Toss! Let's get started!")
answer = input("Remember, 1 is for Heads and 0 is for tails which means you lost. Are you ready to roll your dice? ")
import random
random_roll = random.randint(0,1)
if answer.lower() == "yes": 
    if random_roll == 1:
        print(f"You got {random_roll}! This means you got in! Congratulations!")
    else:
        print(f"I'm so sorry, You got {random_roll}. Try again later, okay?")
else:
    print("Okay, no rush! Come back when you are ready! Hope to see you soon, bye!")