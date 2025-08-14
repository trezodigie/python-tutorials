user = input("Hi! Please type your prefered genre? ").strip().lower()
romance = ["The notebook", "La La land", "Crazy rich asians", "To all the boys I've loved before"]
comedy = ["Game night","Booksmart", "The Hustle", "Palm springs"]
drama = ["1917", "Joker", "Marriage story", "The trials of the Chicago 7"]
thriller = ["Get out", "Knives Out", "Parasite", "Tenet"]
genre = [romance, comedy, drama, thriller]
import random 
if user == "romance":
    options = (random.choice(genre[0]))
    print(f"You should watch: {options}")
elif user == "comedy":
    options = (random.choice(genre[1]))
    print(f"You should watch {options}")
elif user == "drama":
    options = (random.choice(genre[2]))
    print(f"You should watch: {options}")
elif user == "thriller":
    options = (random.choice(genre[2]))
    print(f"You should watch: {options}")
else:
    print("You inputted a genre that is not included. The only available genres are romance, drama, comedy and thriller. Please try again.")
    user = input("Hi! Please type your prefered genre? ").strip().lower()
romance = ["The notebook", "La La land", "Crazy rich asians", "To all the boys I've loved before"]
comedy = ["Game night","Booksmart", "The Hustle", "Palm springs"]
drama = ["1917", "Joker", "Marriage story", "The trials of the Chicago 7"]
thriller = ["Get out", "Knives Out", "Parasite", "Tenet"]
genre = [romance, comedy, drama, thriller]
import random 
if user == "romance":
    options = (random.choice(genre[0]))
    print(f"You should watch: {options}")
elif user == "comedy":
    options = (random.choice(genre[1]))
    print(f"You should watch {options}")
elif user == "drama":
    options = (random.choice(genre[2]))
    print(f"You should watch: {options}")
elif user == "thriller":
    options = (random.choice(genre[2]))
    print(f"You should watch: {options}")