bill = float(input("What was the bill total?\n"))
#Lesson says to ask for values of 10, 12, 15
# but I'm going to make it more flexible
tip_percentage = int(input("How much do you want to tip in percentage?\n"))
total = bill * (1 + tip_percentage/100)

num_of_ppl = int(input("How many people are splitting the check?\n"))
per_person = "{:.2f}".format(total/num_of_ppl, 2)

print(f"Each person owes ${per_person}.")