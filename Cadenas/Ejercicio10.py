# Solicitar al usuario la lista de productos separados por comas
productos = input("Por favor, introduce los productos de la cesta de compra, separados por comas: ")

# Dividir la cadena en productos utilizando la coma como separador
productos_lista = productos.split(',')

# Mostrar cada producto en una línea distinta
for producto in productos_lista:
    print(producto.strip())  # strip() elimina espacios en blanco alrededor de cada producto
