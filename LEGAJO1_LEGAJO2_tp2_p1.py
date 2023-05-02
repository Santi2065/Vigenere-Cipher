'''
Se debe escribir un programa que le pida al usuario el path a un archivo en texto plano,
por ejemplo plain.txt y, con una clave solicitada al usuario, encripte el texto mediante
cifrado de Vigenère y lo guarde en un nuevo archivo elegido por el usuario, por ejemplo encrypted.txt.
Todos los caracteres especiales y números deben quedar como estaban en el texto plano.
Las mayúsculas deben convertirse en minúsculas antes de encriptar, el texto encriptado estará entonces todo en minúscula.
En este caso encriptaremos sólo las 26 letras del alfabeto inglés.
El programa no debe fallar catastróficamente ante entradas insperadas del usuario, archivos vacíos o inexistentes, etc.
'''

def cifrado_vi (texto:str,clave:str)->str:
    '''
    Utilizo el metodo de cifrado de Vigenère
    tomo una cadena de texto y una clave y devuelvo el texto encriptado

    input: 
        texto:str - texto a encriptar
        clave:str - contraseña para encriptar

    output:
        texto_encriptado:str - texto ya encriptado
    '''
    texto=list(texto)
    clave=list(clave)

    #cambio los caracteres de clave a numeros segun el cifrado
    for j in range(len(clave)):
        clave[j]=ord(clave[j])-97
    
    #cambio los caracteres del texto a numeros, le sumo el numero
    #de clave en la posicion correspondiente y transformo a char de vuelta
    for i in range(len(texto)-1):
        if not texto[i]==" ":
            texto[i]=ord(texto[i])-97
            texto[i]=chr(((texto[i]+clave[i%len(clave)-1])%26)+97)
    return "".join(texto)


#Pido la ruta del archivo a encriptar y lo guardo
text_dir=input("Ingrese la ruta del archivo a encriptar: ")

#Pido la clave a utilizar para encriptar
clave=input("Ingrese la clave a utilizar: ")

#chequear si el texto utiliza alfabeto ingles
if not(clave.isalpha()):
    print("La clave solo puede contener letras del alfabeto inglés")
    exit(1)

#pido el nombre del archivo a crear o editar con el texto encriptado
nombre_encriptado=input("Ingrese el nombre del archivo encriptado: ")

with open(text_dir, "r") as archivo:
    #guardo el contenido del archivo en text
    text=archivo.read()

#paso la cadena de texto a minusculas
text=text.lower()
cifrado=cifrado_vi(text,clave)

#escribo lo encriptado en un archivo con el nombre_encriptado
with open(nombre_encriptado,"w") as new_file:
    new_file.write(cifrado)