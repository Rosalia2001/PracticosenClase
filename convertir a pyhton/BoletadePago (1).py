def operacion4 (hb, ba, bt, vc, sd, operacion3):
    lp = (hb+ba+bt+vc+sd)-afp
    print ("Liquido Pagable: ", lp)
    return lp
def operacion3 (sd, hb, bs, bt, vc, operacion2):
    afp = ti + (((hb+ba+bt+vc+sd)/100)*12.71)
    print ("AFP y total egresos: ", afp)
    return afp
def operacion2 (sd, hb, ba, bt, vc, operacion1):
    ti = hb+ba+bt+vc+sd
    print ("Total de ingresos: ", ti)
    return ti
def operacion1 (nd, hb):
    sd = nd*(hb/30)*2
    print ("Salario Dominical: ")
    return sd
def BoletadePago ():
    nom = input("Ingrese su nombre: ")
    ci = input("Ingrese su cedula de identidad: ")
    car = input("Ingrese su cargo: ")
    print ("Ingrese su haber básico: ")
    hb = float(input())
    ma = input("Ingrese el mes actual: ")
    print ("Ingrese años de antiguedad: ")
    aa = int(input())
    te = input("Ingrese el tipo de empresa: ")
    print ("¿Cuantos domingos usted ha trabajado?: ")
    nd = int(input())
    
    ba = 60
    bt = 157.5
    vc = 88

    print("NOMBRE:", nom)
    print("CI:", ci)
    print("Tipo de empresa:", te)
    print("Haber Basico:", hb, "Bs")
    print("Bono de Alimentacion:", ba, "Bs")
    print("Bono de Transporte:", bt, "Bs")
    print("Vales de consumo:", vc, "Bs")