class Computer(object):

 def __init__(self):
   self.__maxprice = 900 # Atributo Privado
   self.minprice = 200 # Atributo Publico

 """
    Definicion de Metodo privado
 """
 def __size(self):
     print("Metodo privado")
 
 """
    Definicion de Metodo Publico
 """
 def sell(self):
   print('Selling Price: {}'.format(self.__maxprice))
   
 def getMaxPrice(self):
    return self.__maxprice

 def setMaxPrice(self, price):
   self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
#c.__size()
print(c.__maxprice)
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()