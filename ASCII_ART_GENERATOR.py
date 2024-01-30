from ASCII_ART_DICT import Ascii_letters

lettersdict = Ascii_letters

letter_width = {letter: max([len(lettersdict[letter].split('\n'))]) for letter in lettersdict}

letter_height = {letter: len(lettersdict[letter].split('\n')) for letter in lettersdict}

for letter, ascii in lettersdict.items():
    new_ascii = []
    for line in ascii.split('\n'):
        if len(line) < letter_width[letter]:
            new_ascii.append(line + " " * (letter_width[letter] - len(line)))
        else:
            new_ascii.append(line)
    lettersdict[letter] = '\n'.join(new_ascii)
        
#print(letter_width)
#print('\n'.join([letter for letter in lettersdict.values()]))

test = input("Enter a string to transform: ")

output = ""

for i in range(6):
    for lettre in test:
        if letter_height[lettre.capitalize()]<6-(6-i-1):
            output += letter_width[lettre.capitalize()]*' '
        else:
            output += lettersdict[lettre.capitalize()].split('\n')[i]
    output += '\n'

print(output)