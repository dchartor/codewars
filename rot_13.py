from string import ascii_lowercase, ascii_uppercase

def rot13(message):
    low = str.maketrans(ascii_lowercase, ascii_lowercase[13:] + ascii_lowercase[:13])
    up = str.maketrans(ascii_uppercase, ascii_uppercase[13:] + ascii_uppercase[:13])

    return message.translate(low).translate(up)
