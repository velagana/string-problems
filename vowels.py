'''Python Program to Accept the Strings Which Contains all Vowels'''
string = input("Enter the string: ")
vowels = 'AEIOUaeiou'
contains_all_vowels = all(vowel in string for vowel in vowels)

if contains_all_vowels:
    print("ACCEPTED")
else:
    print("NOT ACCEPTED")
