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

# Se define una funcion que dada un texto, lo limpia dejandolo como un string sin espacios y en minuscula. La misma se
# utilizara durante el programa.
def text_formatter(texto: str) -> str:
    """
    La funcion text_formatter recibe un texto y lo formatea dejando un 
    string sin espacios ni caracteres no deseados.
    ------------------------------------------------------------------
    input:
        texto -> Texto ha formatear
    ------------------------------------------------------------------
    output:
        texto -> Texto formateado
    """
    clean_text = [] # Creo una lista vacia donde almaceno cada una de las letras deseadas.
    for letra in texto: # Itero en cada letro del texto dado.
        letra = letra.lower()
        if letra.isalpha() and letra != "ñ": 
            clean_text.append(letra) # Si la letra es valida y adecuada, la agrego a la lista 'clean_text'
    clean_text = "".join(clean_text) # Transformo la lista en un texto solo con las letras adecuadas sin espacios.
    return clean_text

# Se define una funcion separador con el fin de crear una lista con 'N' sublistas, agrupadas por cada
# letra del lugar 'N' y sus multiplos hasta el final del texto.
def separador(largo_clave: int,text: list) ->list: 
    """
    La funcion separador recibe dos argumentos que permite separar un texto en 
    una lista con sublistas dentro. Cada sublista agrupa una serie de letras
    en ese 'N' lugar y luego avanza a la proxima posicion salteando de a 'N' espacios.
    ------------------------------------------------------------------------------
    input : 
        largo_clave -> 'N' Frecuencia de avance entre letra y letra
        text -> Texto a separar
    ------------------------------------------------------------------------------
    output :
        text_separado -> Lista con sublistas de letras.
    """
    text_separado = [] # Creamos una lista vacia que va a agrupar a las sublistas.
    for n_lista in range(largo_clave): # Iteramos solo la cantidad de 'N' ingresadas por el usuario.
        sublista = [] # Lista auxiliar que permite almacenar los valores requeridos del texto.
        for index in range(n_lista, len(text), largo_clave): # Iterador por cada 'N'.
            sublista.append(text[index]) # Se agrega la letra en el lugar 'N' a una sublista y se avanzan otros 'N' espacios.
        text_separado.append(sublista) # Se inserta la sublista completa, y se pasa al siguiente 'N'
    return text_separado

# Se define una funcion que dado un texto, crea un diccionario con la cantidad de repeticiones de cada letra del abecedario ingles.
def cuento_repeticion(texto: str) ->dict:
    """
    - La funcion cuento_repeticion recibe un texto y devuelve un diccionario
    con la frecuencia de cada letra del abecedario ingles en el texto.

    - Se analizan unicamente los textos en minuscula, es decir transforma 
    los caracteres del texto a minuscula y evalua en ese contexto.
    -----------------------------------------------------------------------
    input:
        texto -> Texto ha analizar
    -----------------------------------------------------------------------
    output:
        cuento_letras -> Diccionario con frecuencias

    """
    abecedario = "abcdefghijklmnopqrtsuvwxyz" # Defino el abecedario ingles en un string para solo evaluar estas letras.
    cuento_letras = {letra: 0 for letra in abecedario} # Hago un diccionario de comprension para cada letra de 'abecedario'.
    texto = text_formatter(texto)
    for letra in texto: # Iteracion para cada letra del texto.
        cuento_letras[letra]+=1 # Aumento la frecuencia de cada letra a medida que itero en el texto.
    return cuento_letras # Devuelve el diccionario con las frecuencias de cada letra en el texto.

# Se define una funcion que en base a la formula del calculo del ioc, devuelve el ioc de un texto dado.
def calculo_ioc(texto: str) ->float: 
    """
    La funcion 'calculo_ioc' recibe un texto y calcula el indice de coincidencia 
    de un texto en ingles.
    ----------------------------------------------------------------------------
    input:
        texto -> Texto ha calcular indice de coincidencia
    ----------------------------------------------------------------------------
    output:
        ioc -> Indice de coincidencia del texto
    """
    cuento_letras = cuento_repeticion(texto) # Cuento la frecuencia de las letras del texto dado llamando a 'cuento_repeticion'.
    n = len(texto) # Calculo el largo del texto y lo guardo en 'n' porque lo necesito para el calculo del ioc.
    ioc = 0 
    for value in cuento_letras.values(): # Entro en el diccionario creado y utilizo los 'value' para el calculo.
        ioc += value * (value - 1)
    ioc /= n * (n - 1)
    return ioc

# Se define una funcion que dado un diccionario, crea otro diccionario con la frecuencia de cada letra en un texto. 
def frecuencia(letras: dict, texto: str) -> dict:
    abecedario = "abcdefghijklmnopqrtsuvwxyz" # Defino el abecedario ingles para luego trabajar con el mismo.
    texto = text_formatter(texto) # Llamo a la funcion 'text_formatter' que deja el texto como un string sin espacios.
    largo = len(texto) # Calculo el largo del texto.
    frecuencia = {letra: 0 for letra in abecedario} # Hago un diccionario de comprension para cada letra de 'abecedario'.
    for key, value in letras.items(): # Entro a cada llave y valor del diccionario recibido.
        frecuencia[key] = value / largo # Reemplazo el valor del diccionario por la frecuencia calculada con la formula.
    return frecuencia # Devuelve el diccionario con cada una de las frecuencias de cada letra del abecedario ingles en un texto.

# Se define una funcion que recibe un texto 
def ioc_promedio_clave(texto: str, largo_clave: int) ->float:
    cadena = separador(largo_clave, texto)
    ioc_final=0
    for lista in cadena:
        ioc_final+= calculo_ioc("".join(lista))
    return ioc_final/largo_clave

def grafico(elementos:dict,y_lable:str,titulo:str):
    plt.bar(list(elementos.keys()),(elementos.values()))
    plt.title(titulo)
    plt.ylabel(y_lable)
    plt.show()

def main():
    # Grafico 1 - Ingles
    #fig, ax = plt.subplots()
    #ax.bar(list(ENGLISH_LETTERS_FRECUENCIES.keys()),(ENGLISH_LETTERS_FRECUENCIES.values()), label=list(ENGLISH_LETTERS_FRECUENCIES.keys()))
    #ax.set_ylabel('Frecuencia')
    #ax.set_title('Inglés')
    #plt.show() 

    nombre_archivo = input("Ingrese el nombre del archivo que contiene el texto: ")

    with open(nombre_archivo,'r') as texto:
        text = texto.read()
        text = text_formatter(text)
        
    # Grafico ioc
    ioc_largos={n:ioc_promedio_clave(text_analizable,n) for n in range(1,30)}
    grafico(ioc_largos,"índice de coincidencia","ioc")
    # Grafico 1 - Ingles
    grafico(ENGLISH_LETTERS_FRECUENCIES,"Frecuencia","Ingles")
    #resto de graficos
    for largo in range(1,30):
        grafico(frecuencia(text_analizable,largo),"Frecuencia",f"Letra {largo} de la clave")


if __name__=="__main__":
    main()
