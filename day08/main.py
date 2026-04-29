from art import *

print(logo)
#capital A starts from chr(65)
#small a starts from chr(97)

def encode(number, message):
    encoded_message = ""

    for char in message:
        ascii_char_value = ord(char)
        if 64 < ascii_char_value < 91 or 95 < ascii_char_value < 122:
            ciphered_char_ascii = number + ascii_char_value
            encoded_message += chr(ciphered_char_ascii)
        elif char == " ":
            encoded_message += char
        else:
            encoded_message += char
    return encoded_message




def decode(number, message):
    decoded_message = ""
    for char in message:

        ascii_char_value = ord(char)
        if 65 < ascii_char_value < 122:
            deciphered_char_ascii = ascii_char_value - number
            decoded_message += chr(deciphered_char_ascii)
        elif char == " ":
            decoded_message += char
        else:
            decoded_message += char
    return decoded_message

game_is_on = True

while game_is_on:

    type = input("Do you want to encode or decode? ")
    message = input("Enter the message you want to encode or decode? ")
    number = int(input("Enter the shift number:  "))

    if type == "encode":
        cipher_message = encode(number, message)
        print (f"Encoded message is {cipher_message}")
    elif type == "decode":
        decipher_message = decode(number, message)
        print (f"Decoded message is {decipher_message}")

    continue_game = input("Do you want to play again? y/n")
    if continue_game == "n":
        game_is_on = False


