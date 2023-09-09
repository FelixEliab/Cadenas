# Solicitar la fecha de nacimiento en formato dd/mm/aaaa
fecha_nacimiento = input("Por favor, introduce tu fecha de nacimiento (dd/mm/aaaa): ")

# Dividir la fecha en día, mes y año
dia, mes, anio = fecha_nacimiento.split('/')

# Verificar si el día o el mes tienen un solo carácter y agregar un cero si es necesario
if len(dia) == 1:
    dia = '0' + dia
if len(mes) == 1:
    mes = '0' + mes

# Mostrar la fecha formateada
print("Día:", dia)
print("Mes:", mes)
print("Año:", anio)
