def get_valid_number(prompt):
    while True:
        value = input(prompt)
        if value.replace('.', '', 1).isdigit():
            value = float(value)
            if value > 0:
                return value
            else:
                print("The value must be a positive number.")
        else:
            print("Invalid input: Please enter a valid number.")

def capitalize_name(name):
    return name.capitalize()

name = input("Enter your name: ")
name = capitalize_name(name)

weight = get_valid_number("Enter your weight in kilograms: ")
height = get_valid_number("Enter your height in meters: ")

bmi = (weight / (height ** 2))*10000

if bmi > 0:
    if bmi < 18.5:
        print(f"{name}, your BMI is {bmi}. You are underweight!")
    elif bmi < 25:
        print(f"{name}, your BMI is {bmi}. You have a normal weight!")
    elif bmi < 30:
        print(f"{name}, your BMI is {bmi}. You are overweight!")
    elif bmi < 35:
        print(f"{name}, your BMI is {bmi}. You are obese!")
    elif bmi <= 39.9:
        print(f"{name}, your BMI is {bmi}. You are severely obese!")
    elif bmi >= 40:
        print(f"{name}, your BMI is {bmi}. You are morbidly obese!")
else:
    print("Enter valid numbers")
