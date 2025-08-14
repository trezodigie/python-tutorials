# student_scores = input("Kindly input the high scores. ").split()
# for n in range(0,len(student_scores)):
#    student_scores[n] = int(student_scores[n])
# highest = 0
# for i in student_scores:
#     if i > highest:
#         highest = i
# print(f"Highest score = {highest}")
highest = 0
for i in range(0,101,30):
    highest += i
print(f"Total number: {highest}")