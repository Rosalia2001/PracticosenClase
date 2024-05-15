#Impresion de la cantidad total de palabras cada frase
Frase = input("Ingrese una palabra o frase: ")
palabras = Frase.strip()
print("Cantidad de palabras en una frase: ", len(palabras))
contador_a = contador_e = contador_i = contador_o = contador_u = 0

# Imprimir la cantidad de veces que aparece cada vocal (a, e, i, o, u) en la frase.

for caracteres in Frase:
    caracteres = caracteres.lower()
    if caracteres == "a":
        contador_a +=1
    elif caracteres == "e":
        contador_e +=1
    elif caracteres == "i":
        contador_i +=1
    elif caracteres == "o":
        contador_o +=1
    elif caracteres == "u":
        contador_u +=1
print("Cantidad de vocal a", contador_a)
print("Cantidad de vocal e", contador_e)
print("Cantidad de vocal i", contador_i)
print("Cantidad de vocal o", contador_o)
print("Cantidad de vocal u", contador_u)

#Imprimer las frase con todas las palabras en mayúsculas.
FraseMayus = Frase.upper()
print(FraseMayus)
FraseMinus = Frase.lower()
print(FraseMinus)

# Reemplazo vocales con 1 y consonante con 2
def reemplazar_vocales_consonantes(cadena):
    nueva_cadena = ""
    for caracter in cadena:
        if caracter.lower() in "aeiou":
            nueva_cadena += "8"
        elif caracter.isalpha():
            nueva_cadena += "1"
        else:
            nueva_cadena += caracter
    return nueva_cadena

Frase_modificado = reemplazar_vocales_consonantes(Frase)
print (Frase_modificado)

# Interpolacion
Nombre = input("Ingrese su nombre: ")
Edad = input("Ingrese su edad: ")
Ciudad = input("Ingrese su ciudad de residencia: ")
mensaje = "Hola, me llamo {} y tengo {} años. Soy de {}.".format(Nombre,Edad,Ciudad)
print(mensaje)

# Codigo de Verificación

Password = input("Ingrese su contraseña: ")

if len(Password) < 8:
    print("La contraseña debe tener al menos 8 caracteres.")
else:
    contiene_minuscula = False
    contiene_mayuscula = False
    contiene_digito = False
    contiene_signosespeciales = False
    for caracter in Password:
        if caracter.islower():
            contiene_minuscula = True
        elif caracter.isupper():
            contiene_mayuscula = True
        elif caracter.isdigit():
            contiene_digito = True
        elif not caracter.isalnum():
            contiene_signosespeciales = True
    if contiene_minuscula and contiene_mayuscula and contiene_digito and contiene_signosespeciales:
        print("¡La contraseña es validad!")
    else:
        print("La contraseña es invalidad")
        print("¡Requistos no cumplidos!")
        if not contiene_minuscula:
            print("La contraseña debe contener por lo menos una letra minúscula")
        if not contiene_mayuscula:
            print("La contraseña debe contener por lo menos una letra mayúscula")
        if not contiene_digito:
            print("La contraseña debe contener por lo menos un digito")
        if not contiene_signosespeciales:
            print("La contraseña debe contener por lo menos un caracter especial")

