import matplotlib.pyplot as plt
ABECEDARIO="abcdefghijklmnopqrstuvwxyz"
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
        if ord('a') <= ord(letra) <= ord('z'): 
            clean_text.append(letra) # Si la letra es valida y adecuada, la agrego a la lista 'clean_text'
    clean_text = "".join(clean_text) # Transformo la lista en un texto solo con las letras adecuadas sin espacios.
    return clean_text

def text_divisor(text: str, inicio: int, largo_clave: int) -> str:
    texto_final = []
    for index in range(inicio, len(text), largo_clave):
        texto_final.append(text[index])
    return "".join(texto_final)


# Se define una funcion text_multiple_division con el fin de crear una lista con 'N' sublistas, agrupadas por cada
# letra del lugar 'N' y sus multiplos hasta el final del texto.
def text_multiple_division(largo_clave: int,text: list) -> list: 
    """
    La funcion text_multiple_division recibe dos argumentos que permite separar un texto en 
    una lista con sublistas dentro. Cada sublista agrupa una serie de letras
    en ese 'N' lugar y luego avanza a la proxima posicion salteando de a 'N' espacios.
    ------------------------------------------------------------------------------
    input : 
        largo_clave -> 'N' Frecuencia de avance entre letra y letra
        text -> Texto a separar
    ------------------------------------------------------------------------------
    output :
        text_separado -> Lista con strings.
    """
    text_separado = [] # Creamos una lista vacia que va a agrupar a las sublistas.
    for n_lista in range(largo_clave): # Iteramos solo la cantidad de 'N' ingresadas por el usuario.
        sublista = text_divisor(text, n_lista, largo_clave)
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
    cuento_letras = {letra: 0 for letra in ABECEDARIO} # Hago un diccionario de comprension para cada letra de 'abecedario'.
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
    n = len(texto)
    ioc = 0 
    for value in cuento_letras.values(): # Entro en el diccionario creado y utilizo los 'value' para el calculo.
        ioc += value * (value - 1)
    ioc /= (n * (n - 1))
    return ioc

# Se define una funcion que dado un diccionario, crea otro diccionario con la frecuencia de cada letra en un texto. 
def frecuencia(letras: dict, largo_texto:int) -> dict:
    frecuencia = {letra: 0 for letra in ABECEDARIO} # Hago un diccionario de comprension para cada letra de 'abecedario'.
    for key, value in letras.items(): # Entro a cada llave y valor del diccionario recibido.
        frecuencia[key] = value / largo_texto # Reemplazo el valor del diccionario por la frecuencia calculada con la formula.
    return frecuencia # Devuelve el diccionario con cada una de las frecuencias de cada letra del abecedario ingles en un texto.

# Se define una funcion que recibe un texto 
def ioc_promedio_clave(texto: str, largo_clave: int) -> float:
    cadena = text_multiple_division(largo_clave, texto)
    ioc_final = 0
    for string in cadena:
        ioc_final += calculo_ioc(string)
    return ioc_final / largo_clave

def grafico(elementos: dict, y_label: str = "", x_label: str = "", titulo: str = ""):
    plt.bar((elementos.keys()),(elementos.values()))
    plt.title(titulo)
    plt.ylabel(y_label)
    plt.xlabel(x_label)


def main():
    nombre_archivo = input("Ingrese el nombre del archivo que contiene el texto: ")

    with open(nombre_archivo,'r') as texto:
        text = texto.read()
        text = text_formatter(text)
        
    # Grafico ioc
    ioc_largos={n:ioc_promedio_clave(text,n) for n in range(1,31)}
    grafico(ioc_largos,"índice de coincidencia","","ioc")
    plt.axhline(y=0.0686, color='black', linestyle='--', linewidth=2)
    plt.axhline(y=0.0385, color='black', linestyle='--', linewidth=2)
    plt.show()

    # Graficos
    largo_clave=5
    if (largo_clave+1)%3==0:
        columnas=((largo_clave+1)//3)
    else:
        columnas=((largo_clave+1)//3)+1
    # Grafico en ingles
    plt.subplot(3,columnas,1)
    grafico(ENGLISH_LETTERS_FRECUENCIES,"Frecuencia","","Ingles")
    
    #resto de graficos
    inicio=0
    for largo in range(1,largo_clave+1):
        plt.subplot(3,columnas,largo+1)
        grafico(frecuencia(cuento_repeticion(text_divisor(text,inicio,largo_clave)),len(text_divisor(text,inicio,largo_clave))), "Frecuencia", "", f"Letra {largo} de la clave")
        inicio+=1
    plt.tight_layout()
    plt.show()



if __name__=="__main__":
    main()
