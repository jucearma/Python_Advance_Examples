car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
# items - Lista de Tuplas con el par llave valor
x = car.items()
car['year'] = 2018
# Agregar un valor al Diccionario
car['brand'] = 'Chevrolet'
print(x)
# Validar si una Llave Existe en un Dicccionario
if "year" in car.keys():
    print(True)
else:
  print(False)

# Consultar el indece de una llave del Diccionario y lo elimina
car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
car.pop('model')
print(car)
# Retornar el valor para una llave si esta se encuentra en el diccionario, sino retornar
# un valor por defecto. En este caso como no se encuentra la llave "color", retorna "white"
car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
x = car.setdefault('color', 'white')
print(x)

#
car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
del car['model']
print(car)
# Crear copias de un Diccionario
dicc2 = car.copy()
# Eliminar elementos de un Diccionario
car.clear()
