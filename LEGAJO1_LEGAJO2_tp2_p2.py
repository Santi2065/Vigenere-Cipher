def descifrado_vi (texto: str,clave:str)->str:
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
    for j in range(len(clave)):
        clave[j] = ord(clave[j])-97
    
    # Cambio los caracteres del texto a numeros, le resto el numero
    # de clave en la posicion correspondiente y transformo a char(letra) de vuelta.
    for i in range(len(texto)-1):
        if texto[i].isalpha() and texto[i]!='ñ':
            texto[i] = ord(texto[i]) - 97
            texto[i] = chr(((texto[i] - clave[i % len(clave) - 1]) % 26) + 97)
    return "".join(texto)    

def main():
    """
    Se utiliza la funcion 'descifrado_vi' para recibir un archivo
    y crear uno nuevo con el texto desencriptado junto a la interaccion 
    del usuario.
    -------------------------------------------------------------------
    No se reciben argumentos al llamar la funcion.
    -------------------------------------------------------------------
    Interaccion con el usuario:

    -> Ruta del archivo encriptado
    - Se validan ciertos requerimientos

    -> Clave para desencriptacion
    - Se validan ciertos requerimientos

    -> Ruta del nuevo archivo con el texto ya descencriptado
    -------------------------------------------------------------------
    Output:
    -> Generacion del archivo descencriptado con los datos recibidos.
    """
    # Pido la ruta del archivo a desencriptar y lo guardo, y valido que el archivo exista.
    file_check = False
    while not file_check: 
        try:
            text_dir = input("Ingrese la ruta del archivo a desencriptar: ")
            file_check = True
            # Guardo el contenido del archivo en text.
            with open(text_dir, "r") as archivo:
                text = archivo.read()
                if len(text) == 0:
                    print("El archivo está vacío")
                    file_check = False
        except FileNotFoundError: # Atajo el error si el archivo no existe.
            print("No se pudo abrir el archivo")
            file_check = False

    # Pido la clave a utilizar para desencriptar y evaluo su validez.
    pass_valid = False
    while not pass_valid: # Ciclo que permite volver a pedir la clave si esta no es adecuada.
        clave = input("Ingrese la clave a utilizar: ")
        pass_valid = True
        if clave != "":
            for letra in clave:
                if not letra.isalpha() or letra == "ñ":
                    print("La clave solo puede contener letras del alfabeto inglés y no puede contener espacios.")
                    pass_valid=False
                    break
                elif letra.isupper():
                    print("La clave no puede contener mayusuculas.")
                    pass_valid = False
                    break
        else:
            print("Debe escribir una clave")
            pass_valid = False

    # Desencripto el texto.
    cifrado = descifrado_vi(text,clave)

    # Escribo lo desencriptado en un archivo con el nombre_desencriptado.
    nombre_desencriptado = input("Ingrese el nombre del archivo desencriptado: ")
    file_check = True
    with open(nombre_desencriptado,"w") as new_file:
        new_file.write(cifrado)

if __name__=="__main__":
    main()
