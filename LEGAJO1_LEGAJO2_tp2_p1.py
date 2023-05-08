def cifrado_vi (texto: str, clave: str)-> str:
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
    for j in range(len(clave)):
        clave[j] = ord(clave[j])-97
    
    # Cambio los caracteres del texto a numeros, le sumo el numero
    # de clave en la posicion correspondiente y transformo a char(letra) de vuelta.
    for i in range(len(texto)-1):
        if texto[i].isalpha() and texto[i] != 'ñ':
            texto[i] = ord(texto[i])-97
            texto[i] = chr(((texto[i]+clave[i%len(clave)-1])%26)+97)
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
    # Pido la ruta del archivo a encriptar y lo guardo.
    file_check = False
    # Valido que el archivo exista.
    # Pido el nombre del archivo a crear o editar con el texto encriptado.
    while not file_check: #Esto va cuando abrimos el archivo
        try:
            text_dir = input("Ingrese la ruta del archivo a encriptar: ")
            file_check = True
            # Guardo el contenido del archivo en text.
            with open(text_dir, "r") as archivo:
                text = archivo.read()
                if len(text) == 0:
                    print("El archivo está vacío")
                    file_check = False
        except FileNotFoundError:
            print("No se pudo abrir el archivo")
            file_check = False
            
    # Pido la clave a utilizar para encriptar y evaluo su validez.
    pass_valid=False
    while not pass_valid:
        clave = input("Ingrese la clave a utilizar: ")
        pass_valid=True
        if clave != "":
            for letra in clave:
                if not letra.isalpha() or letra == "ñ" or letra == " ":
                    print("La clave solo puede contener letras del alfabeto inglés")
                    pass_valid=False
        else:
            print("Debe escribir una clave")



    # Encripto el texto.
    cifrado = cifrado_vi(text,clave)

    # Escribo lo encriptado en un archivo con el nombre_encriptado.
    nombre_encriptado = input("Ingrese la ruta del archivo encriptado: ")
    file_check=True
    with open(nombre_encriptado,"w") as new_file:
        new_file.write(cifrado)

if __name__ == "__main__":
    main()