height = float(input("Please enter your height in cm:\n"))
weight = float(input("Please enter your weight in kg:\n"))

bmi = weight / (height ** 2)
BMI_UNDERWEIGHT = f"Your BMI is {bmi}, you are underweight."
BMI_NORM_WEIGHT = f"Your BMI is {bmi}, you are normal weight."
BMI_OVER_WEIGHT = f"Your BMI is {bmi}, you are slightly weight."
BMI_OBESE = f"Your BMI is {bmi}, you are obese."
BMI_CLINICALLY_OBESE = f"Your BMI is {bmi}, you are clinically obese"

if bmi < 18.5:
    print(BMI_UNDERWEIGHT)
elif 18.5 <= bmi < 25:
    print(BMI_NORM_WEIGHT)
elif 25 <= bmi < 30:
    print(BMI_OVER_WEIGHT)
elif 30 <= bmi < 35:
    print(BMI_OBESE)
else:
    print(BMI_CLINICALLY_OBESE)
