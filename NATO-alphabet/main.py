import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {
    row.letter: row.code
    for (index, row)
    in data.iterrows()
}
print(phonetic_dict)

is_work = True


def enter_word():
    word_ = input("Enter a word: ").upper()
    if word_ == "Q":
        return word_
    try:
        output_list = [
            phonetic_dict[letter]
            for (letter)
            in word_
        ]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(output_list)


while is_work:
    word = enter_word()
    if word == "Q":
        is_work = False
