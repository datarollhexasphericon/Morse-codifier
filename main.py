from get_morse_codes import morse_dict

# Ask user for input message to code into morse
msg_to_code = input("What do you want to convert to morse code? ").lower()

# Print the morse code corresponding to each character in user message or
# Print character if corresponding morse code not found
for char in msg_to_code:
    print(morse_dict.get(char, char) if char != ' ' else ' ')
