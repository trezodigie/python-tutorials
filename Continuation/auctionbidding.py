#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bidders = {}
print("Welcome to the secret auction program.")
name = input("What is your name? ")
bid = int(input("What is your bid? $"))
others = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
#I struggled so much with knowing what to use. I orignally used if but it was while because if breaks the loop which we don't want
while others == "yes":
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  #I had a lot of errors because I didn't write this bidders[name] = bid to update the dictionary. Whew. That's why it's important to understand the logic first!
  bidders[name]= bid
  others = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  if others == "no":
    break
  
highest_bid = 0
highest_bidder = ""

for bidder in bidders:
  if bidders[bidder] > highest_bid:
    highest_bid = bidders[bidder]
    highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")