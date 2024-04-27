bill = 0
size = input("Welcome to Python Pizza! What size pizza can I get you? S,M or L\n")

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

pepperoni = input("Would you like to add pepperoni? Y or N\n")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

cheese = input("Would you like extra cheese? Y or N\n")

if cheese == "Y":
    bill += 1

print("Thank you for choosing Python Pizza!")
print(f"Your final bill is: ${bill}.")
