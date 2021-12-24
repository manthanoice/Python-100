import pandas as pd

df = pd.read_csv(r'Day-26\nato_phonetic_alphabet.csv')

the_final_dict = {row.letter: row.code for (index, row) in df.iterrows()}
def xoox():
    name = input("Enter your name: ").upper()
    try:
        answer = [the_final_dict[letter] for letter in name]
    except KeyError:
        print('You can only enter alphabets, sorry')
        xoox()
    else:
        print(answer)

xoox()