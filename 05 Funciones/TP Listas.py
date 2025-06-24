# 1) Lista de múltiplos de 4 del 1 al 100
multiplos_de_4 = list(range(4, 101, 4))
print("Múltiplos de 4:", multiplos_de_4)

# 2) Lista con cinco elementos y mostrar el penúltimo
gustos = ["pizza", "python", "música", "bicicleta", "playa"]
print("Penúltimo elemento:", gustos[-2])

# 3) Crear lista vacía, agregar tres palabras con append
palabras = []
palabras.append("hola")
palabras.append("mundo")
palabras.append("Python")
print("Lista de palabras:", palabras)

# 4) Reemplazar segundo y último valor de la lista 'animales'
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("Animales modificados:", animales)

# 5) Explicación del programa
# Crea una lista llamada numeros con los valores [8, 15, 3, 22, 7].
# Encuentra el valor más alto de esa lista con max(numeros), que es 22.
# Elimina ese valor máximo con remove(22), usando remove(max(numeros)).
# Finalmente, imprime la lista modificada, que queda como [8, 15, 3, 7].

# 6) Lista del 10 al 30 con saltos de 5 y mostrar los dos primeros
numeros = list(range(10, 31, 5))
print("Dos primeros:", numeros[:2])

# 7) Reemplazar los dos valores centrales de 'autos'
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "coupe"]
print("Autos modificados:", autos)

# 8) Agregar dobles a una lista vacía usando append
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Dobles:", dobles)

# 9) Operaciones sobre lista de compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print("Compras actualizadas:", compras)

# 10) Crear una lista anidada con valores específicos
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("Lista anidada:", lista_anidada)
