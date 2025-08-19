user = int(input("Please input a number "))
total = 0
for n in range(0,(user + 1),2):
    if user > 1000:
        break
    else:
        total += n
print(total)