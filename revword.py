def reverse_words(input_string):
    # Split the input string into words using space as the separator
    words = input_string.split()

    # Reverse the order of the words
    reversed_words = words[::-1]

    # Join the reversed words back into a string with space as the separator
    reversed_string = ' '.join(reversed_words)

    return reversed_string

# Example usage:
input_string = "Hello World"
result = reverse_words(input_string)
print(result)  # Output will be "World Hello"
