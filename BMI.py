name = input("Enter your Name: ")
while True:
    try:       
        weight = float(input("Enter your Weight (in kg): "))
        height = float(input("Enter your Height (in meters): "))
        
        if weight <= 0 or height <= 0:
            print("Please enter valid details for weight and height.")
            continue

        bmi = weight / (height ** 2)
        print("Your Body Mass Index is:", bmi)

        if 0 < bmi < 18.5:
            print(name, "you are Underweight.")
        elif 18.5 <= bmi < 25:
            print(name, "you have Normal weight.")
        elif 25 <= bmi < 30:
            print(name, "you are Overweight.")
        else:
            print(name, "you are Obese.")

        break
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")
