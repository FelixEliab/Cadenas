# Solicitar el nombre del usuario
nombre_usuario = input("Por favor, introduce tu nombre: ")

# Solicitar un número entero
try:
    numero = int(input("Por favor, introduce un número entero: "))
except ValueError:
    print("El valor introducido no es un número entero válido.")
    exit()

# Imprimir el nombre del usuario tantas veces como el número introducido
for _ in range(numero):
    print(nombre_usuario)
