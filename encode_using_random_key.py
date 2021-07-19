from random import choice, randint
from string import ascii_lowercase, ascii_uppercase

from utils.vigenere import encode

if __name__ == '__main__':
    KEY_LENGTH = randint(4, 10)
    clave = ''.join([choice(ascii_uppercase) for _ in range(KEY_LENGTH)])
    print('LA CLAVE UTILIZADA ES:', clave)
    
    with open('original_text.txt', 'r') as text:
        texto = text.read()
        texto = ''.join(
            [letra for letra in texto if letra in ascii_uppercase + ascii_lowercase])
        texto = texto.upper()
        
    texto_codificado = encode(mensaje=texto, clave=clave)
    with open('encoded_text.txt', 'w') as f:
        f.write(texto_codificado)
