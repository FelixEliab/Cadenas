# Solicitar al usuario que introduzca una frase
frase = input("Por favor, introduce una frase: ")

# Solicitar al usuario que introduzca una vocal
vocal = input("Por favor, introduce una vocal: ")

# Verificar que la entrada sea una sola letra y sea una vocal
if len(vocal) == 1 and vocal.lower() in "aeiou":
    # Reemplazar todas las ocurrencias de la vocal en la frase con la versión en mayúscula
    frase_modificada = frase.replace(vocal, vocal.upper())
    print("Frase con la vocal en mayúscula:", frase_modificada)
else:
    print("La entrada no es una vocal válida o no es una sola letra.")
