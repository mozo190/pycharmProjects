from dictionary import morse_dict


def convert_to_morse(text):
    morse_code = []
    text = text.upper()  # Convert the text to uppercase
    for letter in text:
        if letter in morse_dict:
            morse_code.append(morse_dict[letter])
        else:
            morse_code.append('?')
    return ' '.join(morse_code)


def convert_to_text(morse_code):
    text = []
    morse_code = morse_code.split(' ')
    for code in morse_code:
        if code == '/':
            text.append(' ')
        else:
            for letter, morse in morse_dict.items():
                if code == morse:
                    text.append(letter)
                    break
            else:
                text.append('?')
    return ''.join(text)


def main():
    prompt = input("Enter '1' to convert text to Morse code or "
                   "'2' to convert Morse code to text or"
                   " '3' if you want to quit: ")
    if prompt == '1':
        text = input("Enter the text to convert to Morse code: ")
        converted_text = convert_to_morse(text)
        print(f'The Morse code for "{text}" is: {converted_text}')
    elif prompt == '2':
        more_code = input("Enter the Morse code to convert to text: ")
        converted_code = convert_to_text(more_code)
        print(f'The text for "{more_code}" is: {converted_code}')
    elif prompt == '3':
        print("Goodbye!")
        quit()
    else:
        print("Invalid input. Please try again.")
