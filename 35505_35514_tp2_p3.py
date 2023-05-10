import matplotlib.pyplot as plt
ABECEDARIO = "abcdefghijklmnopqrstuvwxyz"
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

# Se define una funcion que dada un texto, la separa en los lugares correspondientes a lo ingresado por el usuario como argumento.
def text_divisor(text: str, inicio: int, largo_clave: int) -> str:
    """
    La funcion text_divisor, recibe un texto y lo lee, guardando
    los caracteres desde el inicio hasta el final que se encuentran
    en los lugares del largo de clave y sus multiplos naturales.
    -----------------------------------------------------------------
    input: 
        text -> Texto a separar
        inicio -> Indice de letra de arranque
        largo_clave -> Paso de separacion entre letra y letra
    -----------------------------------------------------------------
    output:
        string con las letras agrupadas
    """
    texto_final = [] 
    for index in range(inicio, len(text), largo_clave):
        texto_final.append(text[index]) # Guardamos en una lista todas las letras en los lugares correspondientes.
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
    for letra in texto: 
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
    frecuencia = {letra: 0 for letra in ABECEDARIO} # Hago un diccionario de comprension para cada letra de 'ABECEDARIO'.
    for key, value in letras.items(): 
        frecuencia[key] = value / largo_texto # Reemplazo el valor del diccionario por la frecuencia calculada con la formula.
    return frecuencia # Devuelve el diccionario con cada una de las frecuencias de cada letra del abecedario ingles en un texto.

# Se define una funcion que recibe un texto, lo divide con la funcion 'text_multiple_division' y a cada segmento le calcula el IOC
# sumandolos, y devuelve el promedio de la suma.
def ioc_promedio_clave(texto: str, largo_clave: int) -> float:
    """
    La funcion ioc_promedio_clave recibe como argumento un texto y un 
    largo de clave, y divide el texto en grupos con los caracteres con 
    el largo de clave ingresado. Luego a cada segmento le calcula el 
    Indice de Coincidencia y devuelve el promedio de su suma.
    ---------------------------------------------------------------------
    input:
        texto -> Texto a separar y calcular IOC
        largo_clave -> Grado de separacion (int)
    ---------------------------------------------------------------------
    output:
        float con el promedio de la suma de IOC
    """
    cadena = text_multiple_division(largo_clave, texto)
    ioc_final = 0
    for string in cadena:
        ioc_final += calculo_ioc(string)
    return ioc_final / largo_clave

# Se define una funcion que recibe un diccionario con elementos, y los ubica en un grafico de barras.
def grafico(elementos: dict, y_label: str = "", x_label: str = "", titulo: str = ""):
    """
    La funcion grafico, recibe 4 argumentos que le permite armar un grafico de barras.
    Los argumentos para el grafico estan dados dentro del diccionario, tomando las
    llaves y los valores para los ejes de coordenadas respectivamente.
    ----------------------------------------------------------------------------------
    input:
        elementos -> Diccionario donde las keys van en el eje x y los values en el eje y
        y_label -> Etiqueta del eje y (Ingresar "" si no se desea etiquetado)
        x_label -> Etiqueta del eje x (Ingresar "" si no se desea etiquetado)
        titulo -> Etiqueta del titulo del grafico (Ingresar "" si no se desea etiquetado)
    """
    plt.bar((elementos.keys()),(elementos.values()))
    plt.title(titulo)
    plt.ylabel(y_label)
    plt.xlabel(x_label)

def main():
    """
    La funcion main, pide el archivo encriptado ha analizar y formatea el texto de 
    modo tal que sea analizable. Luego genera dos graficos. El primero con el calculo 
    del IOC del texto, permitiendo descifrar el largo de la contraseña del texto
    encriptado. Y el resto de graficos se crean en base al largo de la contraseña
    definida en la variable 'largo_clave' que se encarga de imprimir el grafico
    de las frecuencias de las letras en ingles definida en el diccionario
    'ENGLISH_LETTERS_FRECUENCIES'. Los mismos sirven como guia para descifrar la 
    contraseña en base a los otros graficos que representan cada letra de la 
    contraseña.
    """
    # Pido la ruta del archivo
    file_check = False
    while not file_check: 
        try: 
            text_dir = input("Ingrese el nombre del archivo que contiene el texto: ")
            file_check = True
            # Guardo el contenido del archivo en text.
            with open(text_dir, "r") as archivo:
                text = archivo.read()
                text = text_formatter(text)
                if len(text) == 0:
                    print("El archivo está vacío")
                    file_check = False
        except FileNotFoundError: # Atajo el error si el archivo no existe.
            print("No se encontro el archivo")
            file_check = False
        except PermissionError: # Atajo el error si hay falta de permisos.
            print("No tiene permisos para leer ese archivo.")
            file_check = False
        except IsADirectoryError:
            print("Esto es un directorio")# Atajo el error si es un directorio
            file_check = False
        
    if len(text) < 60:
        print("El texto no es suficientemente largo para graficar el Indice de Coincidencia")
    else:
        # Grafico del IOC
        ioc_largos = {n: ioc_promedio_clave(text, n) for n in range(1, 31)}
        grafico(ioc_largos, "Indice de coincidencia", "Largo de la clave", "IOC")
        plt.axhline(y = 0.0686, color = 'black', linestyle = '--', linewidth = 1.5)
        plt.axhline(y = 0.0385, color = 'black', linestyle = '--', linewidth = 1.5)
        plt.show()

    # Graficos
    largo_clave = 5
    if (largo_clave + 1) % 3 == 0:
        columnas = ((largo_clave + 1) // 3)
    else:
        columnas = ((largo_clave + 1) // 3) + 1

    # Grafico en ingles
    plt.subplot( 3, columnas , 1)
    grafico(ENGLISH_LETTERS_FRECUENCIES , "Frecuencia", "", "Ingles")
    
    # Resto de graficos
    inicio = 0
    for largo in range( 1, largo_clave + 1):
        plt.subplot( 3, columnas , largo+1)
        subtexto = text_divisor(text ,inicio ,largo_clave)
        grafico(frecuencia(cuento_repeticion(subtexto), len(subtexto)), "Frecuencia", "", f"Letra {largo} de la clave")
        inicio += 1
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
