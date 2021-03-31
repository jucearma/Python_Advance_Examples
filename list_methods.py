list = [1,"Dos",3]
buscar = 1
print (buscar in list)
# Listar el indice del elemento que quiero buscar
if buscar in list:
    print(list.index(3))
else:
  print("No se encuentar el elemento")

# Agregar elementos a una Lista
a = ['apple', 'banana', 'cherry']
b = ['Ford', 'BMW', 'Volvo']
a.append(b)
print(a)
# Numero de veces que se repite un elemento dentro de la lista
fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = fruits.count(9)
print(x)
# Agregar elementos a una Lista dada una posicion especifica
fruits = ['apple', 'banana', 'cherry']
x = fruits.insert(1, 'orange')
print(x)
# Extiende una lista, agregando elementos desde un Iterable
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)
# Extarer y eliminar un elemento de una lista
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)
# Simplemento Eliminar un elemento de una lista
fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits)
# Invertir los elementos de una Lista
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

# Limpiar o borrar los elementos de una Lista
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits)

fruits = ['apple', 'banana', 'cherry']
x = fruits.copy()
print(x)