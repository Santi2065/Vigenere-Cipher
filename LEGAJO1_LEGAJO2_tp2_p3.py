import matplotlib.pyplot as plt
ENGLISH_LETTERS_FRECUENCIES = {
    "a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253, "e": 0.12702, "f": 0.02228,
    "g": 0.02015, "h": 0.06094, "i": 0.06966, "j": 0.00153, "k": 0.00772, "l": 0.04025,
    "m": 0.02406, "n": 0.06749, "o": 0.07507, "p": 0.01929, "q": 0.00095, "r": 0.05987,
    "s": 0.06327, "t": 0.09056, "u": 0.02758, "v": 0.00978, "w": 0.02360, "x": 0.00150,
    "y": 0.01974, "z": 0.00075
}


def separador(n:int,text:list)->list:
    text_separado=[]
    k=0
    for letra in text:
        if letra.isalpha():
            if (k%n)==0:
                text_separado.append(letra)
            k+=1
    return text_separado


def main():
    # Grafico 1 - Ingles
    fig, ax = plt.subplots()
    ax.bar(list(ENGLISH_LETTERS_FRECUENCIES.keys()),(ENGLISH_LETTERS_FRECUENCIES.values()), label=list(ENGLISH_LETTERS_FRECUENCIES.keys()))
    ax.set_ylabel('Frecuencia')
    ax.set_title('Inglés')
    plt.show() 

    nombre_archivo=input("Ingrese el nombre del archivo que contiene el texto: ")

    with open(nombre_archivo,'r') as texto:
        # Hacer diccionario que cuente las veces que aparecen las letras en el texto.
        abecedario = "abcdefghijklmnopqrtsuvwxyz"
        cuento_letras = {letra: 0 for letra in abecedario}

        # Ioc -> Sumatoria
        # n -> Cantidad de letras del texto
        n = 0
        for letra in texto:
            if letra.isalpha() and letra != 'ñ':
                cuento_letras[letra]+=1
                n += 1
        ioc = 0
        for i in range(1,26+1):
            ioc += (cuento_letras[i]*(cuento_letras[i]-1))/(n*(n-1))

if __name__=="__main__":
    main()
