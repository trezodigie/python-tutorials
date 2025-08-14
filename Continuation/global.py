import random
number_guessed = random.randint(1,100)

def compare():
    global lives
    if lives == 0:
        print(f"That means you lose.\nThe number was actually {number_guessed}\nRestart the game again if you want to try again.")
        return
    number = int(input("Make a guess: "))
    if number < number_guessed and lives > 0: 
        lives -= 1
        print(f"Too low.\nGuess again.\nYou have {lives} attempts remaining to guess the number.")
        compare()
    elif number > number_guessed and lives > 0:
        lives -= 1
        print(f"Too high.\nGuess again!\nYou have {lives} attempts remaining to guess the number.")
        compare()
    else:
        print(f"You got it! The answer is {number_guessed}!")
        return


print("Welcome to the Number Guessing game!\nI'm thinking of a number between 1 and 100")
#print(number_guessed)
difficulty = input("Chose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    lives = 10
    print(f"You have {lives} attempts remaining to guess the number.")
    compare()
else:
    lives = 5
    print(f"You have {lives} attempts remaining to guess the number.")
    compare()
