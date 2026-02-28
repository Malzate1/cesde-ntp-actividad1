# Tema: Uso Avanzado de input() y Formateo de Strings

# Ejercicio 1: Pide al usuario que ingrese su color favorito usando input().
# Luego, imprime un mensaje que diga "Tu color favorito es [color]".
# Escribe tu código debajo de esta línea:
color = input("Ingresa tu color favorito: ")
print(f"Tu color favorito es {color}.")
print()


# Ejercicio 2: Pide al usuario que ingrese su ciudad de residencia y su país de 
# origen (en dos variables e inputs separados).
# Luego usa f-strings o concatenación para imprimir un mensaje como: "Vives en [ciudad], [país]".
# Escribe tu código debajo de esta línea:
ciudad = input("Ingresa tu ciudad de residencia: ")
pais = input("Ingresa tu pais de origen: ")

print(f"Vives en {ciudad},{pais}.")
print()

# Ejercicio 3: Pide al usuario que escriba una palabra sencilla y luego imprímela repetida 5 veces
# (Pista: puedes multiplicar cadenas de texto en Python usando el operador *).
# Escribe tu código debajo de esta línea:
frase = input("Ingresa una palabra: ")

for i in range (5):
    print(frase)

