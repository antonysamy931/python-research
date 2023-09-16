if __name__ == '__main__':
    height = input("Enter your height in meter:")
    weight = input("Enter your weight in kg:")
    weight_int = int(weight)
    height_float = float(height)
    bmi = weight_int / height_float ** 2
    bmi_int = int(bmi)
    print(f"Your bmi is {bmi_int}")