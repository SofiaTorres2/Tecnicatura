#Ejercicio 1: Elminar duplicados de una lista
#Escriba un programa donde tenga una lista y que a continuacion
#Elimine los elementos repetidos, por ultimo mostrar la lista.
import math
from itertools import filterfalse

#Creamoos una lista
lista = [1,2,3, "Ariel", 7,7,3, "Alberto", 1, "Ariel", 2, "Alberto"]
#conjunto = set(lista) #convertimos el conjunto de tipo set
#lista = list(conjunto) # convertimos el conjunto a una lista
lista = list(set(lista)) #la conversacion hecha en una sola linea de codigos (eficiente)
print(lista)

#Ejercicio 2: operaciones de conjuntos con linea
#Escriba un programa que tenga 2 listas y que a continuacion
#Cree las siguientes listas (en las que no deben haber repeticion)
# 1 lista de palabras que aparecen en las lineas
# 2 lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas lista

lista1 = [1,2,3,4,5,4,3,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]

#Eliminar los elementos repetidos de ambas listas con conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2 )
solo1 = list(conjunto1 - conjunto2)
solo2 = list(conjunto1 - conjunto2)
interseccion = list(conjunto1 & conjunto2)

print(f"Lista de palabras que aparecen en las listas : {union}")
print(f"Lista de palabras que aparecen en la primera lista, pero no en la segunda : {solo1}")
print(f"Lista de palabras que aparecen en la segunda lista, pero no en la primera : {solo2}")
print(f"Lista de palabras que aparecen en ambas listas : {interseccion}")

#Ejercicio 3: Agregar personajes a una lista
#Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
#Nombre: Aragon
#Clase: Guerrero
# Raza: Dunadan del norte

# Nombre: Gandal f
#Clase: Mago
#Raza: Istar

#Nombre: Legolas
#Clase: Arquero
# Raza: Elfo Sindar

personajes = []

P = {'Nombre': 'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dunadan del Norte'}
personajes.append(P)
P = {'Nombre': 'Gandal f', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(P)
P = {'Nombre': 'Legolas', 'Clase': 'Aruqero' 'Raza':'Istar'}
personajes.append(P)
print(personajes)

#Dada la siguiente tupla
tupla = (13,1,8,3,2,5,8,) # definimos la tupla
#rear una lista que solo incluya los numeros menores a 5
# e imprima por consola [1, 3, 2]

lista = []
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
 print(lista)

 #Ejercicio de matematicaa
 #Para sacar la raiz uadrada de un numero positivo
 numero = int(input('Digite un numero positivo'))
 while numero <0:
     print('Error -> Deberia ser un numero positivo')
     numero = int(input('Digite un numero positivo:'))
print(f'\nsu raiz cuadrada es : {math.sqrt(numero):.2f}')

#Ejeriio 1: llenar una lista
#Llenar una lista con los numeros de 1 al 50, luego mostra
#La lista con el bucle for, los eleementos deben mostrarse
#de la siguiente forma
#1-2-3-4-5-...-50
#lista = []
#1 = 1
#while i <= 50:
#    lista.apppend(1)
#    1 += 1
lista = list(range(1, 51))
for i in lista:
    print(i,end='-')

#Ejercicio 2: Modificar los elementos de una lista
#llenar una lista on los numero del 1 al 10, luego modifiar los
#elementos de una lista multiplicandolos por un valor ingresado por el usuario
lista = list(range(1, 11))
print('Lista Original')
for i in lista:
    print(i, end='-')
valor = int(input('\ndigite un valor a multiplicar: '))
#Multiplicamos todos los elementos de la lista
for indice, i in enumerate(lista):
    lista[indice] *= valor

print(f'Lista final con los elementos multiplicados por {valor}')
for i in lista:
    print(i, end='-')


#Ejercicio 3: inserte elementos y ordenarlos
#pedir numero y meterlos en una lista, cuandi el usuario
#introduzca un numero 0, nuestro programa dejaria de insertar.
#por ultimo, mostrar los numeros ordenados de menor a mayor

lista = []
salir = False
while not salir:
    numero = int(input('digite un numero'))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort()
print(f'Lista ordenada: \n{lista}')

#Ejercicio 4: sumar numeros pares dentro de un rango
#hacer un programa para sumar numeros pares dentroo
#de un rango, por ejemplo:
#                         suma de numeros pares del 2 al 30
#                         suma = 240

a = int(input('Digite de donde va a comenzar la suma'))
b = int(input('Digite hasta donde quiere llegar a sumar'))
suma = 0
for i in range(a+b+1):
    if i % 2 == 0:
        suma += 1
print(f"\La suma de numeros pares dentro del rango es : {suma}")

#Ejercicio 5: factorial de un numero positivo
#hacer un programa para calcular el factorial de un numero positivo

numero = int(input("Digite un numero"))
while numero < 0:
    print("Error -> El numero tiene que ser positivo")
    numero = int(input("Digite un numero: "))
factorial = 1
for i in range(1, numero+1):
    factorial *= i
print(f"\nEl factorial del numero {numero}positivo ingresado es: {factorial}")


