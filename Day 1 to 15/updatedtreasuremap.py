line1 = ["D","S","W"]
line2 = ["B","G","E"]
line3 = ["G","A","F"]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? Column are in letter (A-C) and row (1-3)? ").lower()

# Extract letter and number from the position
letter = position[0]
number = int(position[1]) - 1

# Define a mapping from letters to column indices
column_indices = {'a': 0, 'b': 1, 'c': 2}

# Update the map grid with the treasure position
map[number][column_indices[letter]] = 'X'

# Print the updated map grid
for row in map:
    print(' '.join(row))