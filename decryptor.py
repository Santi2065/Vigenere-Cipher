import os

def descifrado_vi (texto: str,clave: str) ->str:
    """
    Utiliza el metodo de cifrado de Vigenère
    y desencrpita un texto o mensaje encriptado.
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

    # Cambio los caracteres de clave a numeros segun el cifrado.
    for index, caracter in enumerate(clave):
        clave[index] = ord(caracter) - ord('a') # El ord de 'a' permite pasar las letras a un tabla de valores entre 0 y 25.
    
    # Cambio los caracteres del texto a numeros, le resto el numero
    # de clave en la posicion correspondiente y transformo a char(letra) de vuelta.
    index_clave = 0
    for idx_texto, element in enumerate(texto):
        if ord('a') <= ord(element) <= ord('z'):
            texto[idx_texto] = ord(element) - ord('a')
            texto[idx_texto] = chr(((texto[idx_texto] - clave[index_clave % len(clave)]) % 26) + ord('a'))
            index_clave += 1
    return "".join(texto)

"""
Se utiliza la funcion 'cifrado_vi' para recibir un archivo y crear uno nuevo con el texto encriptado junto a la interaccion 
del usuario. En principio, al llamar la funcion main del programa, no se reciben argumentos de entrada. Luego, se ingresa 
la ruta del archivo a encriptar y su respectiva clave. Ambas deben cumplir ciertos requerimientos, y de ser adecuadas, se 
pide al usuario la ruta del archivo donde se va a guardar el texto encriptado.
"""
def main():
    # Pido la ruta del archivo a desencriptar y lo guardo, y valido que el archivo exista.
    file_check = False
    while not file_check: 
        try:
            text_dir = input("Ingrese la ruta del archivo a desencriptar: ")
            file_check = True
            # Guardo el contenido del archivo en text.
            with open(text_dir, "r", encoding="utf-8") as archivo:
                text = archivo.read()
                if len(text) == 0:
                    print("El archivo está vacío")
                    file_check = False
        except FileNotFoundError: # Atajo el error si el archivo no existe.
            print("No se pudo abrir el archivo")
            file_check = False
        except PermissionError: # Atajo el error si hay falta de permisos.
            print("No tiene permisos para leer ese archivo.")
            file_check = False
        except IsADirectoryError:
            print("Esto es un directorio")# Atajo el error si es un directorio
            file_check = False

    # Pido la clave a utilizar para desencriptar y evaluo su validez.
    pass_valid = False
    while not pass_valid: # Ciclo que permite volver a pedir la clave si esta no es adecuada.
        clave = input("Ingrese la clave a utilizar: ")
        pass_valid = True
        if clave != "":
            for letra in clave:
                letra = letra.lower()
                if not (ord('a') <= ord(letra) <= ord('z')):
                    print("La clave solo puede contener letras del alfabeto inglés y no puede contener espacios.")
                    pass_valid = False
                    break
        else:
            print("Debe escribir una clave")
            pass_valid = False

    # Desencripto el texto.
    cifrado = descifrado_vi(text,clave)

    # Escribo lo desencriptado en un archivo con el nombre_desencriptado.
    file_check = False
    while not file_check: 
        try:
            file_check = True
            nombre_desencriptado = input("Ingrese el nombre del archivo desencriptado: ")
            if os.path.isfile(nombre_desencriptado):
                resp = input(f"El archivo {nombre_desencriptado} ya existe, ¿Quiere sobreescribir el archivo {nombre_desencriptado}? y/n: ")
                if resp == "n":
                    file_check = False
                elif resp != "y":
                    print("Respuesta Invalida")
                    file_check = False
            with open(nombre_desencriptado,"w", encoding="utf-8") as new_file:
                new_file.write(cifrado)
        except PermissionError: # Atajo el error si hay falta de permisos.
            print("No tiene permisos para escribir ese archivo")
            file_check = False
        except FileNotFoundError: # Atajo el error si se ingresa un directorio que no existe.
            print("Directorio invalido")
            file_check = False

if __name__=="__main__":
    main()
