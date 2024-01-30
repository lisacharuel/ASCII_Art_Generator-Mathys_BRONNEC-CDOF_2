from ASCII_ART_DICT import Ascii_letters


test = input("Enter a string to transform: ")

print('\n'.join([Ascii_letters[letter.capitalize()] for letter in test]))