import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row['letter']: row['code'] for _, row in data_frame.iterrows()}

word = input("What word would you like to convert to the NATO alphabet?\n")

nato_list = []
for letter in word:
    cap_letter = letter.capitalize()
    nato_list.append(data_dict[cap_letter])

print(nato_list)
