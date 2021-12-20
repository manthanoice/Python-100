import pandas as pd

df = pd.read_csv(r'Day-26\nato_phonetic_alphabet.csv')
the_dict = df.to_dict()

the_final_dict = {row.letter: row.code for (index, row) in df.iterrows()}

name = input("Enter your name: ").upper()
answer = [the_final_dict[letter] for letter in name]
print(answer)