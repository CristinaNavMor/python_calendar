#                                        CALENDARIO
# ----------------------------------------------------------------------------------------------------
# 5. Write a Python program to print the calendar of a given month and year. If you
# feel confident enough, extend it to cover a complete year (See annex)
# ----------------------------------------------------------------------------------------------------

def esBisiesto(anyo):
    bisiesto=False
    if anyo%4==0 and not anyo%100==0 or anyo%400==0:
        bisiesto=True
    return bisiesto

assert(not esBisiesto(2023))
assert(esBisiesto(2012))
assert(esBisiesto(2016))

def computeDaysInMonth(month, year):
    dia=0
    treinta=[4, 6, 9, 11]
    if month==2 and esBisiesto(year)==True:
        dia=29
    elif month in treinta:
        dia=30
    elif month==2:
        dia=28
    elif month>12 or month<1:
        dia=-1
    else:
        dia=31
    return dia

def calcularDiaSemana(dia, mes, anyo):
    dia_semana=[0, 1, 2, 3, 4, 5, 6]

    a=(14-mes)//12
    y=anyo-a
    m=mes+12*a-2
    d=(dia+y+y//4-y//100+y//400+(31*m)//12)%7

    return dia_semana[d]

def crearEspaciosIniciales(primerDiadeSemana):
    cadena_de_espacios=""
    for i in range(primerDiadeSemana):
        cadena_de_espacios+="   "
    return cadena_de_espacios

def crearSemana(dia, diasSemana, numeroDiasDelMes):
    cadenaDias=""
    inicio=dia
    while dia<=diasSemana:
        if dia>=10 and dia<=numeroDiasDelMes:
            cadenaDias+=str(dia)
            cadenaDias+=" "
            dia+=1
        elif dia>numeroDiasDelMes:
            cadenaDias+=" "
            dia+=1
        elif dia<10 and dia==inicio:
            cadenaDias+=" "
            cadenaDias+=str(dia)
            dia+=1
        elif dia<10 and not dia==9: 
            cadenaDias+="  "
            cadenaDias+=str(dia)
            dia+=1 
        else:  
            cadenaDias+="  "
            cadenaDias+=str(dia)
            cadenaDias+=" "
            dia+=1 

    return [cadenaDias, dia]

def crearPortadaMesyAnyo(mes,anyo):
    lista_meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    portada="     "
    portada+=str(lista_meses[mes-1])
    portada+=" "
    portada+=str(anyo)
    return portada

# Introducción de datos: 
print("_"*60)
print("\n")
print("Programa de impresión de calendarios: ")
mesDado=int(input("Introduce un mes: "))
while mesDado<1 or mesDado>12:
     mesDado=int(input("Mes introducido incorrecto. Introduce un mes (entre 1 y 12): "))   
anyoDado=int(input("Introduce un año: "))
print("_"*60)
print("\n")
# Calculo el número de días del mes y en qué día cae el primer día del mes:
num_dias=computeDaysInMonth(mesDado, anyoDado)
primerDiaMes=calcularDiaSemana(1, mesDado, anyoDado)
# Creo portada y cadena de días de la semana
portadaMes=(crearPortadaMesyAnyo(mesDado, anyoDado))
DIASEMANA="do lu ma mi ju vi sá"

#Creo primera semana: 
semana1=(crearEspaciosIniciales(primerDiaMes)+(crearSemana(dia=1, diasSemana=(7-primerDiaMes), numeroDiasDelMes=num_dias)[0]))
indiceDia=crearSemana(dia=1, diasSemana=(7-primerDiaMes), numeroDiasDelMes=num_dias)[1]
semana1_lista=[]
semana1_lista.append(semana1)
semana1_lista.append(indiceDia)

#Añado la primera semana a la lista común
semanasUnidas=[]
semanasUnidas.append(semana1_lista)

#Hago bucle para crear y añadir el resto de semanas a la lista común
semanaAislada=[]
for i in range(1, 6):
    indiceDia=semanasUnidas[i-1][1]
    semanaAislada.append(crearSemana(indiceDia, (indiceDia+6), num_dias))
    semanasUnidas.append(semanaAislada[0])
    semanaAislada=[]

# Printeo
print(portadaMes)
print(str(DIASEMANA))
for i in range (len(semanasUnidas)):
    print(semanasUnidas[i][0])




