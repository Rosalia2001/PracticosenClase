import random

print ("¿Usted tiene tarjeta de credito?")
print ("1. Sí")
print ("2. No")
resp = int (input())
if resp == 1:
    Pin = random.randint(1000, 9999)
    print (Pin)
    print ("Menú")
    print ("1. Deposito")
    print ("2. Retiro")
    print ("3. Ver Saldo")
    print ("4. salir")
    menu = int(input())
    if menu == 1:
        saldin = random.randint(0, 100000)
        print ("Su saldo actual es de: ", saldin)
        print ("Escribe el deposito que desea hacer")
        depos = float(input())
        if depos>0:
            saldof = saldin+depos
            print ("Su saldo final es de: ", saldof)
        else:
            print ("No se puede ingresar numeros negativos")
    elif menu == 2:
        saldin = random.randint(0, 100000)
        print ("Su saldo actual es de: ", saldin)
        print ("Escribe el retiro que desea hacer")
        retiro = float(input())
        if depos>0:
            saldof = saldin-retiro
            print ("Su saldo final es de: ", saldof)
        else:
            print ("No se puede ingresar numeros negativos")
    elif menu == 3:
            saldin = random.randint(0, 100000)
            print ("Su saldo actual es de: ", saldin)
    elif menu == 4:
        
        print ("Gracias por usar el cajero, hasta luego")
elif resp ==2:
    print ("Disculpe, Usted no puede ingresar")