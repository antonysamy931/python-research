if __name__ == '__main__':
    height = float(input("Enter your height in meter:"))
    weight = int(input("Enter your weight in kg:"))

    bmi = round(weight / height ** 2)
    
    if bmi < 18.5:
        print(f"Your bmi is {bmi}, you are underweight.")
    elif bmi >= 18.5 and bmi < 25:
        print(f"Your bmi is {bmi}, you have a normal weight.")
    elif bmi >= 25 and bmi < 30:
        print(f"Your bmi is {bmi}, you are slightly overweight.")
    elif bmi >=30 and bmi < 35:
        print(f"Your bmi is {bmi}, you are obese.")
    else:
        print(f"Your bmi is {bmi}, you are clinically obese.")