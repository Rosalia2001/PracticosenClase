Funcion lp <- Operacion4 ( hd, ba, bt, vc, sd, Operacion3 )
	lp <- (hb+ba+bt+vc+sd)-afp
	escribir "Liquido Pagable: " lp " Bs"
Fin Funcion
Funcion afp <- Operacion3 ( sd, hb, ba, bt, vc, Operacion2 )
	afp <- ti +(((hb+ba+bt+vc+sd)/100)*12.71)
	escribir "AFP y total egresos: " afp " Bs"
Fin Funcion
Funcion ti <- Operacion2 (sd, hb, ba, bt, vc, Operacion1 )
	ti <- hb+ba+bt+vc+sd
	escribir "Total de ingresos: " ti " Bs"
Fin Funcion
Funcion sd <- Operacion1 ( nd, hb )
	sd <- nd *(hb/30)*2
	escribir "Salario Dominical: " sd " Bs"
Fin Funcion


Algoritmo BoletadePagosRefactorizado2 
	definir nom, car, te, ma como caracter
	definir aa, ba, vc, nd, ci Como Entero
	definir hb, bt, sdominical, ti, afp, teg, lp Como Real
	Escribir "Ingrese su nombre"
	leer nom
	escribir "Ingrese su cedula de identidad"
	leer ci
	escribir "Ingrese su cargo"
	leer car
	escribir "Ingrese su haber básico"
	leer hb
	escribir "Ingrese el mes actual"
	leer ma
	escribir "Ingrese años de antiguedad"
	leer aa
	escribir "Ingrese el tipo de empresa"
	leer te
	escribir "¿Cuantos domingos usted ha trabajado?"
	leer nd
	ba <- 60
	bt <- 157.5
	vc <- 88	
	escribir "NOMBRE: " nom
	escribir "CI: " ci
	escribir "Tipo de empresa: " te
	escribir "Haber Basico: " hb " Bs"
	escribir "Bono de Alimentacion: " ba " Bs"
	escribir "Bono de Transporte: " bt " Bs"
	escribir "Vales de consumo: " vc " Bs"
	ValorTotal = Operacion4 ( hd, ba, bt, vc, sd, Operacion3 ( sd, hb, ba, bt, vc, Operacion2 (sd, hb, ba, bt, vc, Operacion1 ( nd, hb ))))
FinAlgoritmo