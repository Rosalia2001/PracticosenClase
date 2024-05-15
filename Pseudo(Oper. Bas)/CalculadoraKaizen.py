import random

def operacion(valeatorio, numayor, numenor):
    if valeatorio == 1:
        result = numayor + numenor
        print("La máquina quiso hacer suma y el resultado es:", result)
    elif valeatorio == 2:
        result = numayor - numenor
        print("La máquina quiso hacer resta y el resultado es:", result)
    elif valeatorio == 3:
        result = numayor * numenor
        print("La máquina quiso hacer multiplicación y el resultado es:", result)
    elif valeatorio == 4:
        result = numayor / numenor
        print("La máquina quiso hacer división y el resultado es:", result)
    elif valeatorio == 5:
        result = numayor ** numenor
        print("La máquina quiso hacer potencia y el resultado es:", result)
    return result

def calculadora_kaizen():
    print ("Ingrese dos numeros")
    num1 = float(input())
    num2 = float(input())
    
    if num1 > num2:
        numayor = num1
        numenor = num2
    else:
        numayor = num2
        numenor = num1

    valeatorio = random.randint(1, 5)
    valor_operacion = operacion(valeatorio, numayor, numenor)
    print("El valor total es:", valor_operacion)