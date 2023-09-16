# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
small = 15
medium = 20
large = 25

pepperoni_small = 2
pepperoni_ml = 3

extra_cheese_rate = 1

if size == 'S':
    bill = small
    if add_pepperoni == 'Y':
        bill += pepperoni_small
    
    if extra_cheese == 'Y':
        bill += extra_cheese_rate

    print(f'Your final bill is: ${bill}')
elif size == 'M':
    bill = medium

    if add_pepperoni == 'Y':
        bill += pepperoni_ml

    if extra_cheese == 'Y':
        bill += extra_cheese_rate

    print(f'Your final bill is: ${bill}')
else:
    bill = large

    if add_pepperoni == 'Y':
        bill += pepperoni_ml

    if extra_cheese == 'Y':
        bill += extra_cheese_rate

    print(f'Your final bill is: ${bill}')