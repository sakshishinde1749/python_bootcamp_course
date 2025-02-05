# message encrypt decrypt project

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt and 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))



def ceasar(original_text, shift_amount, encode_or_decode):

    output_text = ""

    if encode_or_decode == 'decode':
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabets:
            shifted_position = alphabets.index(letter) + shift_amount
            shifted_position %= len(alphabets)
            output_text += alphabets[shifted_position]
        else:
            output_text += letter
    
    print(f"Here is {encode_or_decode}d result: {output_text}")

ceasar(text, shift, direction)