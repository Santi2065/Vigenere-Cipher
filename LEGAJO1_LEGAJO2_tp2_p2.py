"""
Se debe escribir un programa que le pida al usuario el path al archivo encriptado,
por ejemplo llamado encrypted.txt, le solicite al usuario una clave y luego 
desencripte el texto con Cifrado de Vigenère y lo guarde en un nuevo archivo elegido por el usuario, por ejemplo llamado decrypted.txt.
"""
def descifrado_vi (texto:str,clave:str)->str:
    """
    Utilizo el metodo de cifrado de Vigenère
    y desencrpito un texto o mensaje encriptado
    --------------------------------------------------------------------
    input: 
        texto : str - texto a desencriptar
        clave : str - contraseña para desencriptar
    --------------------------------------------------------------------
    output:
        texto_desencriptado : str - texto ya desencriptado
    """
    # Paso la clave y el texto a minuscula y los transformo en listas de chars (Numero relacionado al caracter segun Unicode).
    texto = list(texto.lower())
    clave = list(clave.lower())

    # Cambio los caracteres de clave a numeros segun el cifrado
    for j in range(len(clave)):
        clave[j] = ord(clave[j])-97
    
    # Cambio los caracteres del texto a numeros, le resto el numero
    # de clave en la posicion correspondiente y transformo a char de vuelta.
    for i in range(len(texto)-1):
        if not texto[i] == " ":
            if not texto[i] == "\n":
                texto[i] = ord(texto[i]) - 97
                texto[i] = chr(((texto[i] - clave[i % len(clave) - 1]) % 26) + 97)
    return "".join(texto)    

def main():
    # Pido la ruta del archivo a desencriptar y lo guardo.
    text_dir = input("Ingrese la ruta del archivo a desencriptar: ")

    # Pido la clave a utilizar para desencriptar.
    clave = input("Ingrese la clave a utilizar: ")

    # Chequear si la clave utiliza alfabeto ingles.
    if not(clave.isalpha()):
        print("La clave solo puede contener letras del alfabeto inglés")
        exit(1) # Preguntar a gabi si esta bien el exit, o que usar.

    # Pido el nombre del archivo a crear o editar con el texto desencriptado.
    nombre_desencriptado=input("Ingrese el nombre del archivo desencriptado: ")

    # Guardo el contenido del archivo en text.
    with open(text_dir, "r") as archivo:
        text = archivo.read()
    
    # Chequear si el texto utiliza alfabeto ingles.
    for letra in text:
        if not letra.isalpha() and not letra==" " and not letra=="\n":
            print("El texto solo puede contener letras del alfabeto inglés")
            exit(1)
    
    # Desencripto el texto.
    cifrado = descifrado_vi(text,clave)

    # Escribo lo desencriptado en un archivo con el nombre_desencriptado.
    with open(nombre_desencriptado,"w") as new_file:
        new_file.write(cifrado)

if __name__=="__main__":
    main()
    