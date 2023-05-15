import os

def cifrado_vi (texto: str, clave: str) -> str:
    '''
    Utiliza el metodo de cifrado de Vigenère,
    toma una cadena de texto y una clave y devuelve el texto encriptado.
    --------------------------------------------------------------------
    input: 
        texto: str - texto a encriptar
        clave: str - contraseña para encriptar
    --------------------------------------------------------------------
    output:
        texto_encriptado: str - texto ya encriptado
    '''
    # Paso la clave y el texto a minuscula y los transformo en listas de chars.(Los caracteres tienen un numero asignado universalmente)
    texto = list(texto.lower())
    clave = list(clave.lower())

    # Cambio los caracteres de la clave a numeros segun el cifrado.
    for index, caracter in enumerate (clave):
        clave[index] = ord(caracter) - ord("a") # El ord de 'a' permite pasar las letras a un tabla de valores entre 0 y 25.
    
    # Cambio los caracteres del texto a numeros, le sumo el numero
    # de clave en la posicion correspondiente y transformo a char(letra) de vuelta.
    index_clave = 0 # Defino un contador para llevar la cuenta de letras validas.
    for idx_texto, element in enumerate(texto):
       if ord('a') <= ord(element) <= ord('z'): # Valido que las letras del texto sean adecuadas al abecedario ingles.
            texto[idx_texto] = ord(element) - ord('a') 
            texto[idx_texto] = chr(((texto[idx_texto] + clave[index_clave % len(clave)]) % 26) + ord('a'))
            index_clave += 1 # Aumento el contador de letras validas. 
    return "".join(texto)

"""
Se utiliza la funcion 'cifrado_vi' para recibir un archivo y crear uno nuevo con el texto encriptado junto a la interaccion 
del usuario. En principio, al llamar la funcion main del programa, no se reciben argumentos de entrada. Luego, se ingresa 
la ruta del archivo a encriptar y su respectiva clave. Ambas deben cumplir ciertos requerimientos, y de ser adecuadas, se 
pide al usuario la ruta del archivo donde se va a guardar el texto encriptado.
"""
def main():
    # Pido la ruta del archivo a encriptar y lo guardo, y valido que el archivo exista.
    file_check = False # Defino una variable booleana para luego ir validando ciertos requisitos y poder pedir nuevamente el archivo.
    while not file_check: 
        try: 
            text_dir = input("Ingrese la ruta del archivo ha encriptar: ")
            file_check = True
            # Guardo el contenido del archivo en text.
            with open(text_dir, "r", encoding="utf-8") as archivo:
                text = archivo.read()
                if len(text) == 0:
                    print("El archivo está vacío")
                    file_check = False # Cambiamos el valor de 'file_check' para que vuelva a pedir el archivo.
        except FileNotFoundError: # Atajo el error si el archivo no existe.
            print("No se encontro el archivo")
            file_check = False
        except PermissionError: # Atajo el error si hay falta de permisos.
            print("No tiene permisos para leer ese archivo.")
            file_check = False
        except IsADirectoryError:
            print("Esto es un directorio")# Atajo el error si es un directorio
            file_check = False
            
    # Pido la clave a utilizar para encriptar y evaluo su validez.
    pass_valid = False
    while not pass_valid: # Ciclo que permite volver a pedir la clave en caso de que no sea adecuada.
        clave = input("Ingrese la clave a utilizar: ")
        pass_valid = True # Cambiamos el valor de 'pass_valid' para asumir que la clave es adecuada.
        if clave != "":
            for letra in clave:
                letra=letra.lower()
                if not (ord('a') <= ord(letra) <= ord('z')):
                    print("La clave solo puede contener letras del alfabeto inglés y no puede contener espacios.")
                    pass_valid = False
                    break # Utilizo un break para que apenas encuentre una letra que no es adecuada, vuelva a pedir una nueva contraseña.
        else:
            print("Debe escribir una clave")
            pass_valid = False

    # Encripto el texto.
    cifrado = cifrado_vi(text,clave)

    # Escribo lo encriptado en un archivo con el nombre_encriptado.
    file_check = False
    while not file_check: # Validamos que se pueda escribir en el nuevo archivo. 
        try:
            file_check = True
            nombre_encriptado = input("Ingrese la ruta del archivo encriptado: ") 
            if os.path.isfile(nombre_encriptado):
                resp = input(f"El archivo {nombre_encriptado} ya existe, ¿Quiere sobreescribir el archivo {nombre_encriptado}? y/n: ")
                if resp == "n":
                    file_check = False
                elif resp != "y":
                    print("Respuesta Invalida")
                    file_check = False
            with open(nombre_encriptado,"w", encoding="utf-8") as new_file:
                new_file.write(cifrado)
        except PermissionError: # Atajo el error si hay falta de permisos.
            print("No tiene permisos para escribir ese archivo")
            file_check = False
        except FileNotFoundError: # Atajo el error si se ingresa un directorio que no existe.
            print("Directorio invalido")
            file_check = False

if __name__ == "__main__":
    main()
