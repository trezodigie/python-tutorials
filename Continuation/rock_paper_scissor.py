rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print("Welcome to the Rock Paper Scissors game!")
user = (input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors. "))
#One of Angela's student ways 
# computer = random.randint(0,2)
# choices = [rock, paper, scissors]
# print(choices[user])
# print(choices[computer])
# outcome = ["It's a draw", "You win!", "You lose!"]
# print(outcome[user - computer])

# Another way to do it (my way)
if user == "0":
    user_name = rock
if user == "1":
    user_name = paper
if user == "2":
    user_name = scissors
options = [rock, paper, scissors]
computer = random.choice(options)
if user_name == computer:
    print(f"User: {user_name}")
    print(f"Computer: {computer}")
    print("It's a tie")
elif (user_name == rock and computer == scissors) or (user_name == paper and computer == rock) or (user_name == scissors and computer == paper):
     print(f"user: {user_name}")
     print(f"Computer: {computer}")

     print("You win")
else: 
    print(f"user: {user_name}")
    print(f"Computer: {computer}")
    print("You lose")