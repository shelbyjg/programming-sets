def shift_letter(letter, shift):
    if letter == " ":
        return " "
    else:
        return chr((ord(letter)-ord('A')+shift) % 26+ord('A'))

def caesar_cipher(message, shift):
    def shift_letter(letter, shift):
        if letter == " ":
            return " "
        else:
            return chr((ord(letter)-ord('A')+shift) % 26+ord('A'))

    cipher_message = [ ]
    for letter in message:
        shifted_letter = shift_letter(letter, shift)
        cipher_message.append(shifted_letter)
    return ''.join(cipher_message)

def shift_by_letter(letter, letter_shift):
    def shift_letter(letter, shift):
        if letter == " ":
            return " "
        else:
            return chr((ord(letter)-ord('A')+shift) % 26+ord('A'))

    if letter == " ":
        return " "
    else:
        shift = ord(letter_shift)-ord('A')
        return shift_letter(letter, shift)

def vigenere_cipher(message, key):
    def shift_by_letter(letter, letter_shift):
        def shift_letter(letter, shift):
            if letter == " ":
                return " "
            else:
                return chr((ord(letter)-ord('A')+shift) % 26+ord('A'))
        
        if letter == " ":
            return " "
        else:
            shift = ord(letter_shift)-ord('A')
            return shift_letter(letter, shift)

    key_repeated = (key * ((len(message)//len(key)) + 1))[:len(message)]
    cipher_message = [ ]

    for i in range(len(message)):
        if message[i] == ' ':
            cipher_message.append(' ')
        else:
            cipher_message.append(shift_by_letter(message[i],key_repeated[i]))
    return ''.join(cipher_message)

def scytale_cipher(message, shift):
    while len(message)%shift!=0:
        message+='_' * (shift-len(message)%shift)

    rows = len(message)//shift
    encoded_message = [ ]
    for i in range(len(message)):
        encoded_message.append(message[(i//shift) + (rows * (i%shift))])
    return ''.join(encoded_message)

def scytale_decipher(message, shift):
    columns = len(message)//shift
    decoded_message = [ ]

    for i in range(len(message)):
        decoded_message.append(message[(i%columns) * shift + (i//columns)])
    return ''.join(decoded_message)    