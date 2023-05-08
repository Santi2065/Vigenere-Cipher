'''
Se debe escribir un programa que le pida al usuario el path a un archivo en texto plano,
por ejemplo plain.txt y, con una clave solicitada al usuario, encripte el texto mediante
cifrado de Vigenère y lo guarde en un nuevo archivo elegido por el usuario, por ejemplo encrypted.txt.
Todos los caracteres especiales y números deben quedar como estaban en el texto plano.
Las mayúsculas deben convertirse en minúsculas antes de encriptar, el texto encriptado estará entonces todo en minúscula.
En este caso encriptaremos sólo las 26 letras del alfabeto inglés.
El programa no debe fallar catastróficamente ante entradas insperadas del usuario, archivos vacíos o inexistentes, etc.
'''

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
    file_found = False
    # Valido que el archivo exista.
    while not file_found: 
        try:
            text_dir = input("Ingrese la ruta del archivo a encriptar: ")
            file_found = True
        except FileNotFoundError:
            print("No se pudo abrir el archivo")
            file_found = False
        except FileExistsError:
            print("No se pudo abrir el archivo")
            file_found = False
            
    # Pido la clave a utilizar para encriptar y evaluo su validez.
    clave = input("Ingrese la clave a utilizar: ")
    for letra in clave:
        if not letra.isalpha() or letra == "ñ" or letra == " ":
            print("La clave solo puede contener letras del alfabeto inglés")
            clave = input("Ingrese una nueva clave: ")

    # Pido el nombre del archivo a crear o editar con el texto encriptado.
    nombre_encriptado = input("Ingrese el nombre del archivo encriptado: ")

    # Guardo el contenido del archivo en text.
    with open(text_dir, "r") as archivo:
        text = archivo.read()

    # Encripto el texto.
    cifrado = cifrado_vi(text,clave)

    # Escribo lo encriptado en un archivo con el nombre_encriptado.
    with open(nombre_encriptado,"w") as new_file:
        new_file.write(cifrado)

if __name__ == "__main__":
    main()