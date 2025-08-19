student_heights = input("Kindly input the height of the students. ").split()
for n in range(0,len(student_heights)):
   student_heights[n] = int(student_heights[n])
total = 0
count = 0
for number in student_heights:
      total += number
print(f"Total height: {total}")
for _ in student_heights:
     count += 1 
print(f"Number of students: {count}")
average = round(total/count)
print(f"Average: {average}")