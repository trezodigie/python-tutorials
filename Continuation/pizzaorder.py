print("Thank you for choosing python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M or L? ")
pepperoni = input("Would you want pepperoni on your pizza? Y or N? ")
extracheese = input("What about extra-cheese? Do you want that? Y or N? ")
if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill +=2
    if extracheese == "Y":
        bill +=1
    print(f"Your final bill is ${bill}")
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill +=3
    if extracheese == "Y":
        bill +=1 
    print(f"Your final bill is ${bill}")
else:
    bill = 25
    if pepperoni == "Y":
        bill +=3
    if extracheese == "Y":
        bill +=1
    print(f"Your final bill is ${bill}")

