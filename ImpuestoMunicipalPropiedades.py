materiales_precios = {
    "Asfalto": {"Zona 1": 1190, "Zona 2": 787, "Zona 3": 518, "Zona 4": 341, "Zona 5": 224, "Zona 6": 147, "Zona 7": 100, "Zona 8": 60, "Zona 9": 46, "Zona 10": 37},
    "Adoquin": {"Zona 1": 757, "Zona 2": 518, "Zona 3": 341, "Zona 4": 208, "Zona 5": 136, "Zona 6": 91, "Zona 7": 68, "Zona 8": 54, "Zona 9": 45, "Zona 10": 34},
    "Cemento": {"Zona 1": 1190, "Zona 2": 787, "Zona 3": 518, "Zona 4": 341, "Zona 5": 224, "Zona 6": 147, "Zona 7": 100, "Zona 8": 60, "Zona 9": 46, "Zona 10": 37},
    "Loseta": {"Zona 1": 757, "Zona 2": 518, "Zona 3": 341, "Zona 4": 208, "Zona 5": 136, "Zona 6": 91, "Zona 7": 68, "Zona 8": 54, "Zona 9": 45, "Zona 10": 34},
    "Piedra": {"Zona 1": 476, "Zona 2": 324, "Zona 3": 208, "Zona 4": 136, "Zona 5": 91, "Zona 6": 56, "Zona 7": 46, "Zona 8": 41, "Zona 9": 36, "Zona 10": 25},
    "Ripio": {"Zona 1": 380, "Zona 2": 257, "Zona 3": 168, "Zona 4": 113, "Zona 5": 75, "Zona 6": 46, "Zona 7": 41, "Zona 8": 36, "Zona 9": 30, "Zona 10": 5},
    "Tierra": {"Zona 1": 298, "Zona 2": 208, "Zona 3": 139, "Zona 4": 91, "Zona 5": 59, "Zona 6": 44, "Zona 7": 36, "Zona 8": 34, "Zona 9": 25, "Zona 10": 1},
    "Ladrillo": {"Zona 1": 298, "Zona 2": 208, "Zona 3": 139, "Zona 4": 91, "Zona 5": 59, "Zona 6": 44, "Zona 7": 36, "Zona 8": 34, "Zona 9": 25, "Zona 10": 1}
}

material_eleccion = input("Elige el material en via que tiene su propiedad (Asfalto, Adoquin, Cemento, Loseta, Piedra, Ripio, Tierra, Ladrillo): ")
eleccion_zona = input("Elige que zona te encuetras (Zona 1 a Zona 10): ")

if material_eleccion in materiales_precios and eleccion_zona in materiales_precios[material_eleccion]:
    precio = materiales_precios[material_eleccion][eleccion_zona]
    print(f"El precio del material de {material_eleccion} en la {eleccion_zona} es: {precio} bolivianos")
else:
    print("Respuesta Invalidad (Revise la ortografia)")

def calcular_coeficiente(inclinacion_superficie):
    if inclinacion_superficie >= 0 and inclinacion_superficie <= 10:
        return 1.0
    elif inclinacion_superficie >= 11 and inclinacion_superficie <= 15:
        return 0.90
    elif inclinacion_superficie > 25:
        return 0.80

inclinacion_superficie = float(input("Cuanto son los grados de inclinacion del terreno? "))
coeficiente = calcular_coeficiente(inclinacion_superficie)
print(f"Si la inclinacion de la superfices es de {inclinacion_superficie} grados el coeficiente de inclinacion es de {coeficiente}")

Factores_Servicio = {
    "Energia Electrica": 0.2,
    "Agua Potable": 0.2,
    "Alcantarillado": 0.2,
    "Telefono": 0.2,
    "Minimo": 0.2
}

Eleccion_Servicios = input("Elige los servicios y si son mas de 1 sepera ambos con una coma y luego un espacio(Energia Electrica, Agua Potable, Alcantarillado, Telefono): ").split(", ")

total_factor = sum(Factores_Servicio[servicio] for servicio in Eleccion_Servicios) + Factores_Servicio["Minimo"]
print("El coeficiente total de Factores de existencia de servicos es: ", total_factor)

Superficie = int(input("Introduzca la superficie de la propiedad en metros cuadrados: "))
valor_terrenoM2 = precio * total_factor * coeficiente
print(f"EL VALOR DEL TERRENO POR M2 ES DE Bs.: {valor_terrenoM2}")
Valor_Terreno = valor_terrenoM2 * Superficie
print(f"EL VALOR DE TOTAL DEL TERRENO ES DE Bs: {Valor_Terreno}")


AvaluoTipoPropiedad = {
    "Vivienda Familiar": {"Lujosa": 3502, "Muy Buena": 2336, "Buena": 1556, "Economica": 969, "Interes Social": 574, "Marginal": 94},
    "Propiedad Horizontal": {"Lujosa": 4284, "Muy Buena": 3116, "Buena": 2327, "Economica": 1936}
}

TipoPropiedad = input("Que tipo de propiedad posee? (Vivienda Familiar or Propiedad Horizontal): ")

if TipoPropiedad in AvaluoTipoPropiedad:
    if TipoPropiedad == "Vivienda Familiar":
        TipoConstruccion = input("Que tipo de construccion la propiedad tiene? (Lujosa, Muy Buena, Buena, Economica, Interes Social, Marginal): ")
    else:
        TipoConstruccion = input("Que tipo de construccion la propiedad tiene? (Lujosa, Muy Buena, Buena, Economica): ")

    if TipoConstruccion in AvaluoTipoPropiedad[TipoPropiedad]:
        PrecioM2 = AvaluoTipoPropiedad[TipoPropiedad][TipoConstruccion]
        print(f"El precio por metro cuadrado por tener {TipoPropiedad} de acuerdo con el tipo de contruccion {TipoConstruccion} es Bs. {PrecioM2}")
    else:
        print("Tipo de contruccion invalido.")
else:
    print("Tipo de propiedad invalido")

def coeficiente_dep(antiguedad):
    if 0 <= antiguedad <= 5:
        return 1.0
    elif 6 <= antiguedad <= 10:
        return 0.975
    elif 11 <= antiguedad <= 15:
        return 0.925
    elif 16 <= antiguedad <= 20:
        return 0.900
    elif 21 <= antiguedad <= 25:
        return 0.850
    elif 26 <= antiguedad <= 30:
        return 0.800
    elif 31 <= antiguedad <= 35:
        return 0.750
    elif 36 <= antiguedad <= 40:
        return 0.700
    elif 41 <= antiguedad <= 45:
        return 0.650
    elif 46 <= antiguedad <= 50:
        return 0.600
    elif 51 <= antiguedad <= 999999:
        return 0.550

antiguedad = int(input("Hace cuantos años contruyo su propiedad (ya sea vivienda familiar o propiedad horizontal): "))
Tiempo = coeficiente_dep(antiguedad)
print(f"De acuerdo con la cantidad de {antiguedad} años, su coeficiente de depreciacion es de {Tiempo}")

superficieCons = int(input("Introduzca la superficie construida dentro de la propiedad en metros cuadrados: "))
Valor_Cons = (superficieCons * PrecioM2) * Tiempo
print(f"EL VALOR DE LA SUPERFICIE CONSTRUIDA ES DE Bs: {Valor_Cons}")

Base_Imponible = Valor_Terreno + Valor_Cons
print(f"EL VALOR REAL TOTAL DE LA PROPIEDAD ES DE: {Base_Imponible}")

def couta_fija(limite):
    if 0 <= limite <= 692930:
        couta = 0
        interes = 0.0035
        excedente = 1
        return couta, interes, excedente
    elif 692931 <= limite <= 1385854:
        couta = 2426
        interes = 0.005
        excedente = 692930
        return couta, interes, excedente
    elif 1385855 <= limite <= 2078781:
        couta = 5890
        interes = 0.01
        excedente = 1385854
        return couta, interes, excedente
    elif limite > 2078782:
        couta = 12819
        interes = 0.015
        excedente = 2078781
        return couta, interes, excedente

limite = Base_Imponible
couta, interes, excedente = couta_fija(limite)
PorcetajeBI = round((Base_Imponible - excedente) * interes)
Impuesto = couta + PorcetajeBI
print(f"El MONTO QUE SE DEBE PAGAR EL IMPUESTO A LA PROPIEDAD DE BIENES IMBUEBLES ES DE Bs. {Impuesto}")
