print("The love calculator is calculating your score....")
name1 = input("What is your name? ")
name2 = input("What is your partner's name? ")
combinedname = name1 + name2
lowercase = combinedname.lower()
t = lowercase.count("t")
r = lowercase.count("r")
u = lowercase.count("u")
e = lowercase.count("e")
first_number = t + r + u + e 
l = lowercase.count("l")
o = lowercase.count("o")
v = lowercase.count("v")
e = lowercase.count("e")
second_number = l + o + v + e 
our_number = str(first_number) + str(second_number)
new = int(our_number)
if new < 0 and new > 90:
    print(f"Your score is {new}, you go together like coke and mentos.")
elif new >= 40 and new <= 50:
    print(f"Your score is {new}, you are alright together.")
else:
    print(f"Your score is {new}.")