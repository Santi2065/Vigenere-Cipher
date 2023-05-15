# Vigenere-cipher
1 — Encriptador#

Se debe escribir un programa que le pida al usuario el path a un archivo en texto plano, por ejemplo plain.txt y, con una clave solicitada al usuario,
encripte el texto mediante cifrado de Vigenère y lo guarde en un nuevo archivo elegido por el usuario, por ejemplo encrypted.txt.
Todos los caracteres especiales y números deben quedar como estaban en el texto plano.
Las mayúsculas deben convertirse en minúsculas antes de encriptar, el texto encriptado estará entonces todo en minúscula.
En este caso encriptaremos sólo las 26 letras del alfabeto inglés.
El programa no debe fallar catastróficamente ante entradas insperadas del usuario, archivos vacíos o inexistentes, etc.

2 — Desencriptador#

Se debe escribir un programa que le pida al usuario el path al archivo encriptado, 
por ejemplo llamado encrypted.txt, le solicite al usuario una clave y luego desencripte el texto con Cifrado de Vigenère y lo guarde en un nuevo archivo elegido por el usuario,
por ejemplo llamado decrypted.txt.

3 — Forzar la clave#

Se pide escribir un programa que lea un archivo que le pide al usuario, por ejemplo encrypted.txt y genere los dos gráficos que se piden a continuación.
Análisis de similaridad (Test Friedman)#

Dado un texto en inglés, si se eligen un par de letras al azar, la probabilidad de que estas sean la misma letra es de
. En cambio, si fuera un conjunto de letras completamente al azar la probabilidad de elegir dos y que salga la misma letra sería de

. Esto es lo que se llama el índice de coincidencia (IoC, por sus siglas en inglés).

El índice de coincidencia de un texto se calcula siguiendo la siguiente fórmula
siendo la cantidad de veces que apareció la i-ésima letra del alfabeto en el texto, y

la cantidad de letras del texto.

Para calcular el IoC de un texto suponiendo que está encriptado por una clave de largo

, lo que se puede hacer es:

    Dividir el texto en grupos con las letras separadas por 

    letras entre sí.

    Por ejemplo, si el texto es este es un mensaje súper secreto., y supongo que la clave tiene largo 5, los grupos quedarían:
        {e, s, n, s, s, t}
        {s, u, s, u, e, o}
        {t, n, a, p, c}
        {e, m, j, e, r}
        {e, e, e, r, e}

    Calcular el IoC de cada uno de estos grupos.
    Promediar estos resultados.

Genere un gráfico de barras del IoC en función del posible largo de la clave, para longitudes de entre 1 y 30.

El gráfico debe tener además una linea horizontal en 6.86% y otra en 3.85%

Indice de coincidencia

Para generar los gráficos se debe usar el módulo matplotlib, que típicamente se importa con la siguiente sentencia: import matplotlib.pyplot as plt

Importante

Es posible que antes tenga que correr pip install matplotlib en la terminal para instalar la librería.
Análisis de frecuencias#

Genere una figura que contenga 6 gráficos. El primero debe ser la frecuencia de las letras en el idioma inglés, listadas en el siguiente código:

ENGLISH_LETTERS_FRECUENCIES = {
    "a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253, "e": 0.12702, "f": 0.02228,
    "g": 0.02015, "h": 0.06094, "i": 0.06966, "j": 0.00153, "k": 0.00772, "l": 0.04025,
    "m": 0.02406, "n": 0.06749, "o": 0.07507, "p": 0.01929, "q": 0.00095, "r": 0.05987,
    "s": 0.06327, "t": 0.09056, "u": 0.02758, "v": 0.00978, "w": 0.02360, "x": 0.00150,
    "y": 0.01974, "z": 0.00075
}

Los otros 5 deben ser las frecuencias para el texto de encrypted.txt agrupando de a cada 5 letras.

Es decir:

    La frecuencia de las letras en el idioma inglés.
    La frecuencia de las letras que están en las posiciones 0, 5, 10, 15 … del mensaje en encrypted.txt.
    La frecuencia de las letras que están en las posiciones 1, 6, 11, … del mensaje en encrypted.txt.
    La frecuencia de las letras que están en las posiciones 2, 7, 12, … del mensaje en encrypted.txt.
    La frecuencia de las letras que están en las posiciones 3, 8, 13, … del mensaje en encrypted.txt.
    La frecuencia de las letras que están en las posiciones 4, 9, 14, … del mensaje en encrypted.txt.

Frecuencias de letras

Importante

Cuando se pide las posiciones de las letras del mensaje en encrypted.txt, se refiere a la posición sin contar los espacios ni caracteres especiales.

4 - Romper el código#

Mirando el gráfico de IoC, podemos inferir el largo de la clave. El primer pico alto va a coincidir con el largo de la clave. Los siguiente picos altos coinciden con los armónicos (múltiplos),
es decir, el doble y triple del largo y los picos pequeños con los divisores.

Una vez que conocemos el largo de la clave, tenemos que hacer N gráficos de frecuencias, siendo N el largo de la clave. Ahora,
si miramos estas frecuencias y las comparamos contra las frecuencias de las letras en inglés podemos ver cuál era el corrimiento de cada letra.
Es decir, podemos averiguar la clave que se usó para encriptar. Para probar este punto se puede usar este archivo
