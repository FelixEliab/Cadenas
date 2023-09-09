# Solicitar el número de teléfono
numero_telefono = input("Por favor, introduce el número de teléfono en formato +34-XXXXXXXXX-XX: ")

# Dividir la cadena en partes usando el guión (-) como separador
partes = numero_telefono.split("-")

# Verificar si el formato es correcto
if len(partes) != 3 or partes[0] != "+34":
    print("El formato del número de teléfono no es válido.")
else:
    # Extraer el número de teléfono sin el prefijo y la extensión
    numero_principal = partes[1]
    print("Número de teléfono sin prefijo y extensión:", numero_principal)
