#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.


text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."


def caesar_decrypt(ciphertext: str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    results = []
    length = len(alphabet)

    for shift in range(length):
        decrypted = ''
        for char in ciphertext:
            if char.isalpha():
                index = alphabet.index(char.lower())
                decrypted_char = alphabet[(index - shift)]

                if char.isupper():
                    decrypted += decrypted_char.upper()
                else:
                    decrypted += decrypted_char
            else:
                decrypted += char
        results.append((shift, decrypted))

    return results


decrypted_messages = caesar_decrypt(text)

for shift, message in decrypted_messages:
    print(f'Shift {shift}: {message}')
