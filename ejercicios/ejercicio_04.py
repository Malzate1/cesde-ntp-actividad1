# Tema: Condicionales

# Ejercicio 1: Escribe un programa que verifique si la variable 'numero' es positiva, negativa o cero.
# Imprime un mensaje indicando el resultado.
numero = 7
# Escribe tu código debajo de esta línea:
if numero >= 1:
    print("Es positivo.")
elif numero <= -1:
    print("Es negativo.")
else:
    print("Es igual a 0.")

print()


# Ejercicio 2: Dada la variable 'edad', escribe una condición que imprima "Mayor de edad" 
# si es 18 o mayor, y "Menor de edad" en caso contrario.
edad = 20
# Escribe tu código debajo de esta línea:

if edad >= 18:
    print("Mayor de edad.")
else:
    print("Menor de edad")

print()


# Ejercicio 3: Determina si un número es par o impar usando el operador módulo (%) 
# y muestra un mensaje acordemente.
numero_secreto = 14
# Escribe tu código debajo de esta línea:
if numero_secreto % 2 == 0:
    print("Es par.")
else:
    print("Es impar.")
