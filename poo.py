class Humano:
  def __init__(self, name, age):
    self.name = name
    self.age = age

#pedro = Humano('Pedro',4)
#print(pedro.name)

# HERENCIA
class IngSistemas(Humano):
    def programar(self, lenguaje):
      print ('Voy a programar en', lenguaje)

class LicDerecho(Humano):
    def estudioCaso(self, de):
      print ('Debo estudiar el caso de ', de)

objIngSistemas =  IngSistemas('Pedro',38)
objLicDerecho = LicDerecho('Paola',29)
print("{} el Ingeniero en Sistemas, tiene una edad de {} años".format(objIngSistemas.name,objIngSistemas.age))
print("{} el Licenciado en Derecho, tiene una edad de {} años".format(objLicDerecho.name,objLicDerecho.age))

objIngSistemas.programar('Python')
objLicDerecho.estudioCaso('Pedro')

class Bird:

   def __init__(self):
     print('Bird is ready')

   def whoisThis(self):
     print('Bird')

   def swim(self):
     print('Swim faster')

# child class
class Penguin(Bird):

   def __init__(self):
     # call super() function
     super().__init__()
     print('Penguin is ready')

   def whoisThis(self):
     print('Penguin')

   def run(self):
     print('Run faster')

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

