#Sentencia match
dia = int(input("ingrese el numero del dia: "))#1 para lunes, 2 para martes, etc
if dia == 1:    
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")    
elif dia == 4:         
    print("Jueves") 
elif dia == 5:
        print("Viernes")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("Número de día incorrecto")

#sentencia match
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Número de día incorrecto")