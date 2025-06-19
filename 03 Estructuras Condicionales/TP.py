
# Ejercicio 1: Determinar si el usuario es mayor de edad.
edad = int(input("Ejercicio 1 - Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
else:
    print("No se especifica acción, pero se asume que no es mayor de edad")

print("-" * 50)


# Ejercicio 2: Evaluar si la nota es aprobatoria.
nota = float(input("Ejercicio 2 - Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

print("-" * 50)


# Ejercicio 3: Verificar que el número ingresado sea par.
numero = int(input("Ejercicio 3 - Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

print("-" * 50)


# Ejercicio 4: Clasificar la edad en categorías.
edad_categoria = int(input("Ejercicio 4 - Ingrese su edad para clasificar: "))
if edad_categoria < 12:
    categoria = "Niño/a"
elif 12 <= edad_categoria < 18:
    categoria = "Adolescente"
elif 18 <= edad_categoria < 30:
    categoria = "Adulto/a joven"
else:
    categoria = "Adulto/a"
print("La categoría es:", categoria)

print("-" * 50)


# Ejercicio 5: Validar longitud de contraseña.
password = input("Ejercicio 5 - Ingrese una contraseña de entre 8 y 14 caracteres: ")
if 8 <= len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

print("-" * 50)


# Ejercicio 6: Estadísticas sobre una lista aleatoria y determinar sesgo.
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print("Ejercicio 6 - Números aleatorios:", numeros_aleatorios)

# Calcular moda, mediana y media
try:
    mod_val = mode(numeros_aleatorios)
except Exception as e:
    # En caso de haber más de un valor más frecuente, se puede elegir el primero.
    mod_val = None
    print("No se pudo calcular una moda única:", e)
med_val = median(numeros_aleatorios)
mean_val = mean(numeros_aleatorios)

print("Media:", mean_val)
print("Mediana:", med_val)
if mod_val is not None:
    print("Moda:", mod_val)
else:
    print("Moda: No se pudo determinar una moda única.")

# Determinar sesgo
if mod_val is None:
    sesgo = "No se pudo determinar el sesgo debido a la ambigüedad en la moda"
elif mean_val > med_val > mod_val:
    sesgo = "Sesgo positivo (a la derecha)"
elif mean_val < med_val < mod_val:
    sesgo = "Sesgo negativo (a la izquierda)"
elif mean_val == med_val == mod_val:
    sesgo = "Sin sesgo"
else:
    sesgo = "No se cumple ninguno de los criterios clásicos de sesgo"

print("Resultado de sesgo:", sesgo)

print("-" * 50)


# Ejercicio 7: Modificar un string si termina en vocal.
frase = input("Ejercicio 7 - Ingrese una frase o palabra: ")
if frase and frase[-1].lower() in "aeiou":
    frase_modificada = frase + "!"
else:
    frase_modificada = frase
print("Resultado:", frase_modificada)

print("-" * 50)


# Ejercicio 8: Transformar el nombre según la opción elegida.
nombre = input("Ejercicio 8 - Ingrese su nombre: ")
print("Opciones:")
print("1. Nombre en mayúsculas")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra en mayúscula")
opcion = input("Ingrese el número de opción (1, 2, o 3): ")

if opcion == "1":
    resultado = nombre.upper()
elif opcion == "2":
    resultado = nombre.lower()
elif opcion == "3":
    resultado = nombre.title()
else:
    resultado = "Opción no válida. No se realizó transformación"
print("Resultado:", resultado)

print("-" * 50)


# Ejercicio 9: Clasificar un terremoto según la magnitud.
magnitud = float(input("Ejercicio 9 - Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    clasificacion = "Muy leve"
elif 3 <= magnitud < 4:
    clasificacion = "Leve"
elif 4 <= magnitud < 5:
    clasificacion = "Moderado"
elif 5 <= magnitud < 6:
    clasificacion = "Fuerte"
elif 6 <= magnitud < 7:
    clasificacion = "Muy Fuerte"
else:  # magnitud >= 7
    clasificacion = "Extremo"
print("Clasificación:", clasificacion)

print("-" * 50)


# Ejercicio 10: Determinar la estación según hemisferio, mes y día.
hemi = input("Ejercicio 10 - ¿En qué hemisferio se encuentra? (N para Norte / S para Sur): ").strip().upper()

mes = int(input("Ingrese el número del mes (1 a 12): "))
dia = int(input("Ingrese el día: "))

# Función para determinar la estación en el hemisferio norte:
def estacion_norte(mes, dia):
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        return "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        return "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        return "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        return "Otoño"
    else:
        return "Fecha no válida"

# Para el hemisferio sur se intercambian las estaciones según la tabla:
def estacion_sur(mes, dia):
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        return "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        return "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        return "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        return "Primavera"
    else:
        return "Fecha no válida"

if hemi == "N":
    estacion = estacion_norte(mes, dia)
elif hemi == "S":
    estacion = estacion_sur(mes, dia)
else:
    estacion = "Hemisferio no reconocido. Use N o S."

print("La estación del año es:", estacion)