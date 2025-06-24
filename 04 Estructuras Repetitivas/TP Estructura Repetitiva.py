# 1. Imprimir números del 0 al 100
for i in range(101):
    print(i)

# 2. Contar dígitos de un número
num = input("2. Ingresa un número entero: ")
print("Cantidad de dígitos:", len(num.lstrip("-")))

# 3. Sumar enteros entre dos valores
a = int(input("3. Valor 1: "))
b = int(input("   Valor 2: "))
print("Suma intermedia:", sum(range(min(a, b) + 1, max(a, b))))

# 4. Sumar números hasta ingresar 0
total = 0
while True:
    n = int(input("4. Ingresa un número (0 para terminar): "))
    if n == 0:
        break
    total += n
print("Total acumulado:", total)

# 5. Juego de adivinanza
import random
secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("5. Adivina el número (0 a 9): "))
    intentos += 1
    if intento == secreto:
        break
print("¡Correcto! Intentos:", intentos)

# 6. Números pares en orden decreciente
for i in range(100, -1, -2):
    print(i)

# 7. Suma hasta un número ingresado
n = int(input("7. Número positivo: "))
print("Suma total:", sum(range(n + 1)))

# 8. Clasificación de 100 números
pares = impares = positivos = negativos = 0
for _ in range(100):
    n = int(input("8. Ingresa un número: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n >= 0:
        positivos += 1
    else:
        negativos += 1
print("Pares:", pares, "Impares:", impares, "Positivos:", positivos, "Negativos:", negativos)

# 9. Calcular media de 100 números
total = 0
for _ in range(100):
    total += int(input("9. Número: "))
print("Media:", total / 100)

# 10. Invertir los dígitos de un número
n = input("10. Número: ")
print("Invertido:", n[::-1])
