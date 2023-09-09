# Solicitar el correo electrónico al usuario
correo_usuario = input("Por favor, introduce tu correo electrónico: ")

# Dividir el correo electrónico en dos partes: nombre y dominio
nombre, dominio = correo_usuario.split('@')

# Comprobar si el dominio original es válido (debe ser diferente de "ceu.es")
if dominio == "ceu.es":
    print("El dominio ya es 'ceu.es'.")
else:
    # Crear un nuevo correo electrónico con el mismo nombre y el dominio "ceu.es"
    nuevo_correo = f"{nombre}@ceu.es"
    print("Nuevo correo electrónico:", nuevo_correo)
