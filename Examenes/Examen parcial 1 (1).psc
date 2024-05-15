Algoritmo sin_titulo
	Definir NOMBRE,CI,CARGO,TIPODEEMPRESA Como Caracter
	Definir HABERBASICO,Domingos Como Real
	Escribir 'Nombre y Apellido'
	Leer NOMBRE
	Escribir 'Numero de Cedula de Indentidad'
	Leer CI
	Escribir '¿Que Cargo tiene dentro de la empresa?'
	Leer CARGO
	Escribir 'Tipo de empresa en la cual trabaja'
	Leer TIPODEEMPRESA
	Escribir '¿Cual es su haber Basico? (solo en numeros)'
	Leer HABERBASICO
	Escribir '¿Cuantos Domingos Trabajo? (solo en numeros)'
	Leer Domingos
	Si Domingos>0 Entonces
		SalarioDominical <- Domingos*(HABERBASICO/30)*2
	SiNo
		SalarioDominical <- 0
	FinSi
	BonoAlimentacion <- 60
	BonoTransporte <- 157.5
	ValesConsumo <- 88
	TotalIngresos <- HABERBASICO+BonoAlimentacion+BonoTransporte+ValesConsumo+SalarioDominical
	AFP <- TotalIngresos*0.1271
	TotalEgresos <- AFP
	LiquidoPagable <- TotalIngresos-TotalEgresos
	Escribir 'Boleta de Pago'
	Escribir 'Nombre:',NOMBRE
	Escribir 'CI: ',CI
	Escribir 'Cargo:',CARGO
	Escribir 'Tipo de Empresa:',TIPODEEMPRESA
	Escribir 'Haber Basico:',HABERBASICO
	Escribir 'Bono de Alimentacion:',BonoAlimentacion
	Escribir 'Bono de Transporte:',BonoTransporte
	Escribir 'Vales de Consumo:',ValesConsumo
	Escribir 'Salario Dominical:',SalarioDominical
	Escribir 'Total de Ingresos:',TotalIngresos
	Escribir 'AFP:',AFP
	Escribir 'Total Egresos:',TotalEgresos
	Escribir 'Liquido Pagable:',LiquidoPagable
FinAlgoritmo
