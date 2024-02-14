def main(string, key): # the main function, this is where most of the code lives
    decoded_string = '' # an empty string variable is created
    for char in string: # the code will iterate through every character in the given string
        decoded_string += ''.join(chr(ord(char) ^ key)) # the code will XOR every character with the given key, and add these characters in the empty string initialised above

    return decoded_string # then the code will return the completed string


string = str(input("Enter the string to decrypt: ")) # ask the user for encrypted text
key = int(input("Enter the key: ")) # ask the user for a key
flag = main(string, key) # call the main function and pass the result to the flag variable
print(flag) # print the flag variable on the console
    