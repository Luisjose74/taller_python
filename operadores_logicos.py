# operadores logicos
# AND
print (True and True) #si ambos son verdaderos = true
print (True and False) #si uno es falso = false
print (False and True) #si uno es falso = false
print (False and False) #si ambos son falsos = false
# OR
print (True or True) #si ambos son verdaderos = true
print (True or False) #si uno es falso = true
print (False or True) #si uno es falso = true
print (False or False) #si ambos son falsos = false
# NOT
print (not True) #si es verdadero = false
print (not False) #si es falso = true

#Ejercicio AND
print (5>3 and 2<4) # True
print (5>3 and 2>4) # False
print (2>3 and 2<4) # False
print (2>3 and 5<4) # False 
#Ejercicio OR
print (5!=3 or 2<4) # True
print (5>3 or 2==4) # True   
print (2>=3 or 2<=4) # True
print (2>3 or 5<4) # False
#Ejercicio NOT
print (not 5>3) # False
print (not 5<3) # True