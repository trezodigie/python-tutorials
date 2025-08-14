data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States' 
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal' 
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States' 
    },
    {
        'name': 'Kevin Hart',
        'follower_count': 89,
        'description': 'Comedian and actor',
        'country': 'United States' 
    },
    {
        'name': 'Katy Perry',
        'follower_count': 94,
        'description': 'Musician',
        'country': 'United States' 
    },
    {
        'name': 'Kourtney Kardashian',
        'follower_count': 90,
        'description': 'Reality TV personality',
        'country': 'United States' 
    }, 
    {
        'name': 'Camilla Cabello',
        'follower_count': 49,
        'description': 'Musician',
        'country': 'Cuba'
    }, 
    {
        'name': 'NBA',
        'follower_count': 47,
        'description': 'Club Basketball Competition',
        'country': 'United States' 
    
    }, 
    {
        'name': 'Virat Kohli',
        'follower_count': 55,
        'description': 'Cricketer',
        'country': 'India' 
    }, 
    {
        'name': 'Emma Watson',
        'follower_count': 56,
        'description': 'Actress',
        'country': 'United Kingdom' 
    }, 
]

def repeat():
    global player_A, player_B
    player_A = player_B
    player_B = random.choice(data)
    print(f"Compare A: {player_A['name']}, a {player_A['description']}, from {player_A['country']}\nAgainst B: {player_B['name']}, a {player_B['description']}, from {player_B['country']}")
    answer = input("Who has more followers? A or B: ").lower()
    compare (player_A= player_A, player_B=player_B, answer= answer)

def compare(player_A, player_B, answer):
    if player_A['follower_count'] >= player_B['follower_count']:
        correct_answer = "a"
    elif player_A['follower_count'] <= player_B['follower_count']:
        correct_answer = "b"
    global user_score
    
    if answer == correct_answer:
        user_score += 1
        print(f"You are right! Current score: {user_score}")
        repeat()
    else:
        print(f"Sorry, that's wrong. Final score is {user_score}.")
    
# Here, I used a import.sample. This is the first time I'm using it so it's a bit strange but it got the work done. I had to convert data to a list though.
import random
user_score = 0
player_A, player_B = random.sample(data,2)
print("Welcome to the Higher Lower Game!")
repeat()
