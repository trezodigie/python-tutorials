line1 = ["D","S","W"]
line2 = ["B","G","E"]
line3 = ["G","A","F"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? Column are in letter (A-C) and row (1-3)? ").lower()
if position == "a1":
    line1[0] = "X"
    print(f"{line1}\n{line2}\n{line3}")
if position == "b1":
    line1[1] = "X"
    print(f"{line1}\n{line2}\n{line3}")
if position == "c1":
    line1[2] = "X"
    print(f"{line1}\n{line2}\n{line3}")
if position == "a2":
    line2[0] = "X"
    print(f"{line1}\n{line2}\n{line3}")
if position == "b2":
    line2[1] = "X"
    print(f"{line1}\n{line2}\n{line3}")
if position == "c2":
    line2[2] = "X"
    print(f"{line1}\n{line2}\n{line3}")
if position == "a3":
    line3[0] = "X"
    print(f"{line1}\n{line2}\n{line3}")
if position == "b3":
    line3[1] = "X"
    print(f"{line1}\n{line2}\n{line3}")
if position == "c3":
    line3[2] = "X"
    print(f"{line1}\n{line2}\n{line3}")
