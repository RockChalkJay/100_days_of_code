print("Welcome to the Love Calculator. Let's see if you are a match....")

name1 = input("What's your name?").lower()
name2 = input("Who's your crush?").lower()

score1 = 0
score2 = 0
combined_names = name1+name2

score1 += combined_names.count('t')
score1 += combined_names.count('r')
score1 += combined_names.count('u')
score1 += combined_names.count('e')

score2 += combined_names.count('l')
score2 += combined_names.count('o')
score2 += combined_names.count('v')
score2 += combined_names.count('e')

combined_score = int(str(score1) + str(score2))

if combined_score < 10 or combined_score > 90:
    print(f"Your score is {combined_score}, you go together like coke and mentos.")
elif 40 < combined_score < 50:
    print(f"Your score is {combined_score}, you are alright together.")
else:
    print(f"Your score is {combined_score}.")