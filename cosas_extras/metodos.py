# # # ALGUNOS METODOS/FUNCIONES INTEGRADAS EN PYTHON # # #

# capitalize() convierte la primera letra de la cadena en mayúscula y el resto en minúsculas.
nombre = input("ingresa tu nombre: ").capitalize()
print(nombre)

# title() hace lo mismo que capitalize()
nombre = input("Ingresa tu nombre: ").title()
print(nombre)

# upper() convierte todas las letras a mayúsculas
nombre = input("Ingresa tu nombre: ").upper()
print(nombre)

# lower() convierte todas las letras a minúsculas
nombre = input("Ingresa tu nombre: ").lower()
print(nombre)

# swapcase() convierte las mayúsculas en minúsculas y viceversa
nombre = input("Ingresa tu nombre: ").swapcase()
print(nombre)

# strip() elimina los espacios en blanco al principio y al final de la cadena
texto = input("Ingresa un texto: ").strip()
print(texto)

# replace() reemplaza una subcadena por otra en la cadena
texto = input("Ingresa un texto: ").replace("2022", "2023")
print(texto)

# center() centra la cadena dentro de un campo de ancho especificado
texto = input("Ingresa un texto: ").center(20, "_")
print(texto)

# como imprimir un string que contenga comillas
print("\"hola\"")
print('"hola"')

# min() devuelve el valor minimo  |  max() devuelve el valor maximo
# sum() devuelve la suma de todos los valores | len() devuelve la longitud o numero de elementos
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(min(numeros))  # Imprime 1
print(max(numeros))  # Imprime 9
print(sum(numeros))  # Imprime 39
print(len(numeros))  # Imprime 10