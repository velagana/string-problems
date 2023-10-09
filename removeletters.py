'''How to Remove Letters From a String in Python'''



''' Input: 'Geeks123For123Geeks'
Output: GeeksForGeeks
Explanation: In This, we have removed the '123' character from a string.'''

string = input("Enter the string: ")
new_string = ''
for i in string:
    if i != '1' and i != '2' and i != '3':
        new_string += i
print(new_string)



