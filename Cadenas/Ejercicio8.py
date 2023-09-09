# Solicitar el precio del producto en euros con dos decimales
precio = input("Por favor, introduce el precio del producto en euros (con dos decimales): ")

# Convertir la entrada a un número de punto flotante
try:
    precio_float = float(precio)
except ValueError:
    print("La entrada no es un número válido.")
    exit()

# Extraer la parte entera (euros) y decimal (céntimos)
euros = int(precio_float)
centimos = int((precio_float - euros) * 100)

# Mostrar el resultado
print("Número de euros:", euros)
print("Número de céntimos:", centimos)
