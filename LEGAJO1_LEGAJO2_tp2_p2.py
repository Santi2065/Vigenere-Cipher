"""
Se debe escribir un programa que le pida al usuario el path al archivo encriptado,
por ejemplo llamado encrypted.txt, le solicite al usuario una clave y luego 
desencripte el texto con Cifrado de Vigenère y lo guarde en un nuevo archivo elegido por el usuario, por ejemplo llamado decrypted.txt.
"""
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
    # Pido la ruta del archivo a desencriptar y lo guardo.
    file_found = False
    # Valido que el archivo exista.
    while not file_found: 
        try:
            text_dir = input("Ingrese la ruta del archivo a desencriptar: ")
            file_found = True
        except FileNotFoundError:
            print("No se pudo abrir el archivo")
            file_found = False
        except FileExistsError:
            print("No se pudo abrir el archivo")
            file_found = False

    # Pido la clave a utilizar para desencriptar y evaluo su validez.
    clave = input("Ingrese la clave a utilizar: ")
    for letra in clave:
        if not letra.isalpha() or letra == "ñ" or letra == " ":
            print("La clave solo puede contener letras del alfabeto inglés")
            clave = input("Ingrese una nueva clave: ")
    
    # Pido el nombre del archivo a crear o editar con el texto desencriptado.
    nombre_desencriptado = input("Ingrese el nombre del archivo desencriptado: ")

    # Guardo el contenido del archivo en text.
    with open(text_dir, "r") as archivo:
        text = archivo.read()
   
    # Desencripto el texto.
    cifrado = descifrado_vi(text,clave)

    # Escribo lo desencriptado en un archivo con el nombre_desencriptado.
    with open(nombre_desencriptado,"w") as new_file:
        new_file.write(cifrado)

if __name__=="__main__":
    main()
