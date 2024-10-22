def caesar_cipher(text: str) -> str:
    result = ''
    shift = 1

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr(start + (ord(char) - start + shift) % 26)
            result += shifted_char
        else:
            result += char

    return result
