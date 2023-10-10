string = input("Enter the string: ")
i = int(input("Enter the position (i) to remove: "))

if 0 <= i < len(string):
    # Remove the i-th character using slicing
    string = string[:i] + string[i + 1:]
    print("String after removing character at position", i, ":", string)
else:
    print("Invalid position. Position i should be between 0 and", len(string) - 1)
