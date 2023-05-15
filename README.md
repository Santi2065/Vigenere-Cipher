## Vigenere-cipher

### Encryptor

Encrypts a plain text file using the Vigenère cipher with a user-specified key, saving the encrypted text to a new file.

### Decryptor

Decrypts an encrypted text file using the Vigenère cipher with a user-specified key, saving the decrypted text to a new file.

### Key brute-forcing

Analyzes the similarity of an encrypted text and generates graphs:

1. Similarity Analysis (Friedman Test): Calculates the Index of Coincidence (IoC) for different key lengths and plots a graph.

2. Frequency Analysis: Compares letter frequencies in the encrypted text with those in the English language and generates a visualization.

### Breaking the code

Identifies the key length by analyzing the IoC graph and performs frequency analysis to determine the key used for encryption.

The code, graphs, and further details can be found in the [Vigenere-cipher GitHub repository](https://github.com/Santi2065/Vigenere-Cipher).

**Note:** Make sure to install the required library `matplotlib` by running `pip install matplotlib` in your terminal.

Feel free to contribute and enhance the Vigenere-cipher tool!

![Vigenere-cipher](vigenere_cipher_image.jpg)
