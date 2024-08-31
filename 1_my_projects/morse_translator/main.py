# Morse dictionary
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}


def convert_to_morse(text):
    morse_code = []
    text = text.upper()  # Convert the text to uppercase
    for letter in text:
        if letter in morse_dict:
            morse_code.append(morse_dict[letter])
        else:
            morse_code.append('?')
    return ' '.join(morse_code)


def main():
    text = input("Enter the text to convert to Morse code: ")
    converted_text = convert_to_morse(text)
    print(f'The Morse code for "{text}" is: {converted_text}')


if __name__ == "__main__":
    main()
