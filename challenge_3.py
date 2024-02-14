def main(string, key):
    decoded_string = ''
    for char in string:
        decoded_string += ''.join(chr(ord(char) ^ key))

    return decoded_string


string = str(input("Enter the string to decrypt: "))
# string = "je#zlvq#gllqafoo#qjmdp#bmg#wkfqf$p#mlalgz#wkfqf#wkbw#tbp#ml#nbqwjbm#jw$p#kbooltffm"
key = int(input("Enter the key: "))
flag = main(string, key)
print(flag)
    