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
    for index,caracter in enumerate (clave):
        clave[index] = ord(caracter)-ord("a") # El ord de 'a' permite pasar las letras a un tabla de valores entre 0 y 25.
    
    # Cambio los caracteres del texto a numeros, le sumo el numero
    # de clave en la posicion correspondiente y transformo a char(letra) de vuelta.
    index_clave=0
    for idx_texto,element in enumerate(texto):
        if ord('a') <= ord(element) <= ord('z'):
            texto[idx_texto] = ord(element) - ord('a')
            texto[idx_texto] = chr(((texto[idx_texto] + clave [index_clave % len(clave)]) % 26) + ord('a'))
            index_clave+=1
    return "".join(texto)



def main():
    """
    Se utiliza la funcion 'cifrado_vi' para recibir un archivo
    y crear uno nuevo con el texto encriptado junto a la interaccion 
    del usuario.
    ------------------------------------------------------------------
    No se reciben argumentos al llamar la funcion.
    ------------------------------------------------------------------
    Interaccion con el usuario:

    -> Ruta del archivo ha encriptar
    - Se validan ciertos requerimientos

    -> Clave para encriptacion
    - Se validan ciertos requerimientos

    -> Ruta del nuevo archivo luego de ser encriptado
    ------------------------------------------------------------------
    Output:
    -> Generacion del archivo encriptado con los datos recibidos.
    """
    # Pido la ruta del archivo a encriptar y lo guardo, y valido que el archivo exista.
    file_check = False
    while not file_check: 
        try: 
            text_dir = input("Ingrese la ruta del archivo a encriptar: ")
            file_check = True
            # Guardo el contenido del archivo en text.
            with open(text_dir, "r") as archivo:
                text = archivo.read()
                if len(text) == 0:
                    print("El archivo está vacío")
                    file_check = False
        except FileNotFoundError: # Atajo el error si el archivo no existe.
            print("No se encontro el archivo")
            file_check = False
        except PermissionError: # Atajo el error si hay falta de permisos.
            print("No tiene permisos para leer ese archivo.")
            file_check = False
            
    # Pido la clave a utilizar para encriptar y evaluo su validez.
    pass_valid = False
    while not pass_valid: # Ciclo que permite volver a pedir la clave en caso de que no sea adecuada.
        clave = input("Ingrese la clave a utilizar: ")
        pass_valid = True
        if clave != "":
            for letra in clave:
                if not (ord('a') <= ord(letra) <= ord('z')):
                    print("La clave solo puede contener letras del alfabeto inglés y no puede contener espacios.")
                    pass_valid = False
                    break
                elif letra.isupper():
                    print("La clave no puede contener mayusuculas.")
                    pass_valid = False
                    break
        else:
            print("Debe escribir una clave")
            pass_valid = False

    # Encripto el texto.
    cifrado = cifrado_vi(text,clave)

    # Escribo lo encriptado en un archivo con el nombre_encriptado.
    file_check = False
    while not file_check: 
        try:
            nombre_encriptado = input("Ingrese la ruta del archivo encriptado: ")
            with open(nombre_encriptado,"w") as new_file:
                new_file.write(cifrado)
            file_check = True
        except PermissionError: # Atajo el error si hay falta de permisos.
            print("No tiene permisos para escribir ese archivo.")
            file_check = False

if __name__ == "__main__":
    main()