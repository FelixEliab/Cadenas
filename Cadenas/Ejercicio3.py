# Solicitar el nombre del usuario
nombre_usuario = input("Por favor, introduce tu nombre: ")

# Calcular la longitud del nombre
numero_letras = len(nombre_usuario)

# Mostrar el resultado formateado
resultado = f"{nombre_usuario.upper()} tiene {numero_letras} letras."
print(resultado)
