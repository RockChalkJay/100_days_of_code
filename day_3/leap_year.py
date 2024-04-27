year = int(input("Enter a year and I'll tell you if its a leap year\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It's a leap year")
        else:
            print("It's NOT a leap year")
    else:
        print("It's a leap year")
else:
    print("It's NOT a leap year")