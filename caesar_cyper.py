alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def encrypt(original_text, shift_amount):
    encoded_text = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            encode_position = position + shift_amount
            if encode_position <= 25:
                encoded_text += alphabet[encode_position]
            elif encode_position > 25:
                encoded_text += alphabet[encode_position%len(alphabet)]
    print(encoded_text)

def decrypt(original_text, shift_amount):
    decoded_text = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            decode_position = position - shift_amount
            if decode_position <= 25:
                decoded_text += alphabet[decode_position]
    print(decoded_text) 

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)