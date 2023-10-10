def least_frequent_character(input_string):
    # Create a dictionary to store character frequencies
    char_count = {}
    
    # Count the frequency of each character in the string
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the character with the minimum frequency
    min_freq_char = None
    min_freq = float('inf')  # Initialize with a large value
    
    for char, freq in char_count.items():
        if freq < min_freq:
            min_freq = freq
            min_freq_char = char
    
    return min_freq_char

# Example usage:
input_string = "banana"
result = least_frequent_character(input_string)
print(f"The least frequent character in '{input_string}' is '{result}'")