# Tema: Ciclos

# Ejercicio 1: Escribe un programa que utilice un ciclo (for o while) para imprimir todos 
# los números del 1 al 10.
# Escribe tu código debajo de esta línea:

for i in range(1,11):
    print(i)

print()


# Ejercicio 2: Utiliza un ciclo for para imprimir todos los números pares del 2 al 10 inclusive.
# Escribe tu código debajo de esta línea:

for i in range(2,11,2):
    print(i)
print()




# Ejercicio 3: Usa un ciclo while para calcular la suma de los números del 1 al 5. Imprime el 
# resultado final (debe ser 15).
# Escribe tu código debajo de esta línea:
suma =0
num=1

while num <=5:
    suma = suma + num
    num = num + 1

print(f"La suma es igual a {suma}.")



