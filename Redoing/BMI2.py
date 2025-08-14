print("Welcome to the BMI calculator!")
height = input("What is your height in meters? ")
weight = input("Great! What is your weight in kg? ")
height_int = float(height)
weight_int = int(weight)
BMI = round(weight_int/ (height_int **2),2)
if BMI < 18.5:
    print(f"Your BMI is {BMI}, and you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, and you have a normal weight.")  
elif BMI < 30:
    print(f"Your BMI is {BMI}, and you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, and you are obese.")
else:
    print(f"Your BMI is {BMI}, and you are clinically obese.")