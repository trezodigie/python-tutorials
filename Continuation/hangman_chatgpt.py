import random

# List of words to choose from
word = ["salvation", "subterfuge", "operations", "manager", "baboon"]

# Choose a random word
chosen_word = random.choice(word)
print(f"Hi. The chosen word is {chosen_word}")

# Initialize 'new' to represent the word with underscores
new = ['_' for _ in chosen_word]

# Display the initial state of the word
print(" ".join(new))

# Initialize lives
lives = 6

# Game loop
while "_" in new and lives > 0:
    guess = input("Guess a letter: ").lower()

    # Flag to track if guess is correct
    found_match = False

    # Check each letter in chosen_word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            new[position] = letter
            found_match = True

    # If no match found, deduct a life
    if not found_match:
        lives -= 1
        print(f"Incorrect guess! Lives remaining: {lives}")

    # Display current state of the word
    print(" ".join(new))

# End of game
if "_" not in new:
    print("Congratulations! You guessed the word:", chosen_word)
else:
    print("Sorry, you ran out of lives. The word was:", chosen_word)
