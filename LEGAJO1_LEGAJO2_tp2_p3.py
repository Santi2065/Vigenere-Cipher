import matplotlib.pyplot as plt
"""
una posible estructura para tu el programa:

    1.Primero, puedes definir una función para calcular el índice de coincidencia (IoC) de un texto. Esta función tomará como argumento una cadena de texto y devolverá el IoC calculado según la fórmula que se proporciona en la consigna.

    2.Luego, puedes definir una función para calcular el IoC promedio para un posible largo de clave. Esta función tomará como argumentos una cadena de texto y un entero que representa el posible largo de la clave. La función dividirá el texto en grupos con las letras separadas por n letras entre sí (donde n es el posible largo de la clave), calculará el IoC de cada uno de estos grupos y devolverá el promedio de estos resultados.

    3.Después, puedes definir una función para generar el gráfico de barras del IoC en función del posible largo de la clave. Esta función tomará como argumento una cadena de texto y usará las funciones definidas anteriormente para calcular el IoC promedio para cada posible largo de clave entre 1 y 30. Luego, usará matplotlib para generar un gráfico de barras con estos datos.

    4.A continuación, puedes definir una función para calcular las frecuencias de las letras en un texto. Esta función tomará como argumento una cadena de texto y devolverá un diccionario con las frecuencias de cada letra en el texto.

    5.Luego, puedes definir una función para generar la figura que contiene 6 gráficos. Esta función tomará como argumento una cadena de texto y usará la función definida anteriormente para calcular las frecuencias de las letras en el idioma inglés y en el texto agrupando de a cada 5 letras. Luego, usará matplotlib para generar los 6 gráficos con estos datos.

    5.Finalmente, puedes definir la función main que manejará la interacción con el usuario. Esta función pedirá al usuario la ruta del archivo encriptado, leerá el contenido del archivo y llamará a las funciones definidas anteriormente para generar los gráficos requeridos.
"""
ENGLISH_LETTERS_FRECUENCIES = {
    "a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253, "e": 0.12702, "f": 0.02228,
    "g": 0.02015, "h": 0.06094, "i": 0.06966, "j": 0.00153, "k": 0.00772, "l": 0.04025,
    "m": 0.02406, "n": 0.06749, "o": 0.07507, "p": 0.01929, "q": 0.00095, "r": 0.05987,
    "s": 0.06327, "t": 0.09056, "u": 0.02758, "v": 0.00978, "w": 0.02360, "x": 0.00150,
    "y": 0.01974, "z": 0.00075
}


def separador(largo_clave: int,text: list) ->list: # Divide un texto en n listas con letras equiespaciadas en n 
    text_separado = []
    for n_lista in range(largo_clave):
        sublista = []
        for index in range(n_lista, len(text), largo_clave):
            sublista.append(text[index])
        text_separado.append(sublista)
    return text_separado

def cuento_repeticion(texto:str)->dict:# crea diccionario con la cantidad de letras repetidas que tiene un texto.
    abecedario = "abcdefghijklmnopqrtsuvwxyz"
    cuento_letras = {letra: 0 for letra in abecedario}
    for letra in texto:
        cuento_letras[letra]+=1
    return cuento_letras

def ioc_calc(texto:str)->float: 
    cuento_letras = cuento_repeticion(texto)
    print(cuento_letras)
    n = len(texto)
    ioc = 0
    for value in cuento_letras.values():
        ioc += (value*(value-1))
    return ioc/(n*(n-1))

def ioc_promedio_clave(texto:str,largo_clave:int)->float:
    cadena=separador(largo_clave, texto)
    ioc_final=0
    for lista in cadena:
        ioc_final+=ioc_calc("".join(lista))
    return ioc_final/largo_clave

#def grafico(texto:str):

def frecuencia(letras:dict,largo:int)->dict:
    abecedario = "abcdefghijklmnopqrtsuvwxyz"
    frecuencia= {letra: 0 for letra in abecedario}
    for key, value in letras.items():
        frecuencia[key]=value/largo
    return frecuencia




def main():
    # Grafico 1 - Ingles
    #fig, ax = plt.subplots()
    #ax.bar(list(ENGLISH_LETTERS_FRECUENCIES.keys()),(ENGLISH_LETTERS_FRECUENCIES.values()), label=list(ENGLISH_LETTERS_FRECUENCIES.keys()))
    #ax.set_ylabel('Frecuencia')
    #ax.set_title('Inglés')
    #plt.show() 

    nombre_archivo=input("Ingrese el nombre del archivo que contiene el texto: ")

    with open(nombre_archivo,'r') as texto:
        text=texto.read()
    #le saco los caracteres que no se analizan    
    text_analizable=[]

    for letra in text:
        if letra.isalpha() and letra!="ñ":
            text_analizable.append(letra)
    text_analizable="".join(text_analizable)

    print(text_analizable)

if __name__=="__main__":
    main()
