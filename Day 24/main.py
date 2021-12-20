# Day 24
# Date : 20 Dec 2021 
# NATO Aphabet 


import pandas

data = pandas.read_csv("Day 26/NATO-alphabet/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
