if __name__ == "__main__":
    print("Welcome to tip calculator")
    bill = float(input("What was your total bill? $"))
    tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
    person = int(input("How many people to split the bill? "))

    tip_percent = tip / 100
    total_tip_amount = bill * tip_percent
    total_bill_amount = bill + total_tip_amount
    bill_per_person = total_bill_amount / person
    bill_per_person_round = round(bill_per_person, 2)
    bill_per_person_round = '{:.2f}'.format(bill_per_person_round)
    print(f"Each person should pay ${bill_per_person_round}")