if __name__ == "__main__":
    age = input("Enter your age: ")

    age_int = int(age)
    remaining_years = 90 - age_int
    remaining_months = remaining_years * 12
    remaining_weeks = remaining_years * 52
    remaining_days = remaining_years * 365

    message = f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left"
    print(message)