#                                        CALENDARIO
# ----------------------------------------------------------------------------------------------------
# 5. Write a Python program to print the calendar of a given month and year. If you
# feel confident enough, extend it to cover a complete year (See annex)
# ----------------------------------------------------------------------------------------------------


# --------------- Funciones comunes ---------------
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

# --------------- Funciones calendario mes ---------------
def crearEspaciosIniciales(primerDiadeSemana):
    cadena_de_espacios=""
    for i in range(primerDiadeSemana):
        cadena_de_espacios+="   "
    return cadena_de_espacios

def crearSemanaCalendarioMes(dia, diasSemana, numeroDiasDelMes):
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

def obtenerMes():
    # Calculo el número de días del mes y en qué día cae el primer día del mes:
    num_dias=computeDaysInMonth(mesDado, anyoDado)
    primerDiaMes=calcularDiaSemana(1, mesDado, anyoDado)

    #Creo primera semana: 
    semana1=(crearEspaciosIniciales(primerDiaMes)+(crearSemanaCalendarioMes(dia=1, diasSemana=(7-primerDiaMes), numeroDiasDelMes=num_dias)[0]))
    indiceDia=crearSemanaCalendarioMes(dia=1, diasSemana=(7-primerDiaMes), numeroDiasDelMes=num_dias)[1]
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
        semanaAislada.append(crearSemanaCalendarioMes(indiceDia, (indiceDia+6), num_dias))
        semanasUnidas.append(semanaAislada[0])
        semanaAislada=[]

    return semanasUnidas

# --------------- Funciones para calendario completo ---------------
def crearEspaciosFinales(ultimoDiaMes, month, year):
    diaSemana=calcularDiaSemana(ultimoDiaMes, month, year)
    diasFinales=6-diaSemana
    cadena_de_espacios=""
    for i in range(diasFinales):
        cadena_de_espacios+="   "
    return cadena_de_espacios

def crearSemanaCalendarioCompleto(dia, diasSemana, numeroDiasDelMes, mes, anyo):
    cadenaDias=""
    inicio=dia
    while dia<=diasSemana:
        if dia>=10 and dia<=numeroDiasDelMes and dia!=inicio:
            cadenaDias+=" "            
            cadenaDias+=str(dia)
            dia+=1
        elif dia>=10 and dia<=numeroDiasDelMes and dia==inicio:          
            cadenaDias+=str(dia)
            dia+=1           
        elif dia<10 and dia==inicio:
            cadenaDias+=" "
            cadenaDias+=str(dia)
            dia+=1
        elif dia<10 and not dia==9: 
            cadenaDias+="  "
            cadenaDias+=str(dia)
            dia+=1 
        elif dia==(numeroDiasDelMes+1):
            cadenaDias+=crearEspaciosFinales(numeroDiasDelMes, mes, anyo)
            dia=diasSemana+1
        elif inicio>numeroDiasDelMes: # Para poner el final del mes
            cadenaDias+="                    "
            dia=diasSemana+1 #Para que salga del calendario
        elif dia>(numeroDiasDelMes+1): #Creo que este sería prescindible, porque ya lo fuerzo a salir cuando pongo el final de la semana con números, y al iniciar una nueva semana, lo volvería a echar con el de antes. 
            dia=diasSemana+1  #Para que salga del calendario
        else:  
            cadenaDias+="  "
            cadenaDias+=str(dia)
            dia+=1 

    return [cadenaDias, dia]

def crearEncabezadoAnyo(anyo):
    encabezado="                              "
    encabezado+=str(anyo)
    return encabezado

def crearEncabezadoMes(mes):
    lista_meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    encabezado="     "
    encabezado+=str(lista_meses[mes-1])
    return encabezado

# Recojo la información de los meses: número de mes; días del mes; día de la semana en el que empieza el primer día del mes. 
def informacion_de_Meses():
    todos_los_meses=[]
    mes_actual=[]
    for i in range(1,12+1):
        mes_actual.append(i)
        num_dias=computeDaysInMonth(i, anyoDado)
        mes_actual.append(num_dias)
        primerDiaMes=calcularDiaSemana(1, i, anyoDado)
        mes_actual.append(primerDiaMes)
        todos_los_meses.append(mes_actual)
        mes_actual=[]
    return todos_los_meses

#CREO LA PORTADA DE LOS MESES (por fila): 
def crearEncabezadoMeses(indice):
    lista_meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    primer_mes_fila=indice
    encabezado_meses=""
    for i in range(indice+1, indice+4):
        if i==primer_mes_fila+1:
            encabezado_meses+="        "
            encabezado_meses+=str(lista_meses[i-1])
        else: 
            encabezado_meses+="                "
            encabezado_meses+=str(lista_meses[i-1])
    return encabezado_meses

    # Añado la primera semana a la cadena común de primeras semanas de una fila de meses

def crear_calendario_un_mes(primerDiaMes, num_dias, month, year):
    semana1=(crearEspaciosIniciales(primerDiaMes)+(crearSemanaCalendarioCompleto(dia=1, diasSemana=(7-primerDiaMes), numeroDiasDelMes=num_dias, mes=month, anyo=year)[0]))
    indiceDia=crearSemanaCalendarioCompleto(dia=1, diasSemana=(7-primerDiaMes), numeroDiasDelMes=num_dias, mes=month, anyo=year)[1]
    semana1_lista=[]
    semana1_lista.append(semana1)
    semana1_lista.append(indiceDia)

    semanasUnidas=[]
    semanasUnidas.append(semana1_lista)
    # Hago bucle para crear y añadir el resto de semanas a la lista común
    semanaAislada=[]
    for i in range(1, 6):
        indiceDia=semanasUnidas[i-1][1]
        semanaAislada.append(crearSemanaCalendarioCompleto(indiceDia, (indiceDia+6), num_dias, month, year))
        semanasUnidas.append(semanaAislada[0])
        semanaAislada=[]
    return semanasUnidas


# --------------- Introducción de datos ---------------  
print("_"*60)
print("\n")
print("Programa de impresión de calendarios. ")
print("a. Ver calendario de un mes y año concretos.")
print("b. Ver calendario de un año.")
print("c. Salir.")
# Validar la opción del menú
opcion = input("Elige una opción (a, b o c): ").strip().lower()

while opcion not in ['a', 'b', 'c']:
    opcion = input("Opción incorrecta. Elige 'a' para calendario de mes y año, 'b' para calendario de año y 'c' para salir: ").strip().lower()
# Si elige la opción 'b' (ver calendario de un mes y año concretos)
while opcion in ['a', 'b']:

    if opcion == 'a':
        #Introducción de datos y validaciones
        mesDado=input("Introduce un mes: ")
        while not mesDado.isdigit() or int(mesDado)<1 or int(mesDado)>12:
            mesDado=input("Mes introducido incorrecto. Introduce un número entre 1 y 12 para indicar el mes: ") 
        mesDado = int(mesDado)
        anyoDado=input("Introduce un año: ")
        # Validar que el año sea un número entero
        while not anyoDado.isdigit():
            anyoDado = input("Año introducido incorrecto. Introduce un año válido (número): ")
        anyoDado = int(anyoDado)
        print("_"*60)
        print("\n")
        
        DIASEMANA="do lu ma mi ju vi sá"
        # Creo portada y cadena de días de la semana
        portadaMes=(crearPortadaMesyAnyo(mesDado, anyoDado))   

        # Obtengo array de las semanas 
        semanas = obtenerMes()

        # Printeo
        print(portadaMes)
        print(str(DIASEMANA))
        for i in range (len(semanas)):
            print(semanas[i][0])
    else:
        #Introducción de datos y validaciones
        anyoDado=input("Introduce un año: ")
        while not anyoDado.isdigit():
            anyoDado = input("Año introducido incorrecto. Introduce un año válido (número): ")
        anyoDado = int(anyoDado)

        print("_"*60)
        print("\n")    

        # Creo portada y cadena de días de la semana
        encabezadoAnyo=(crearEncabezadoAnyo(anyoDado))
        DIASEMANA="do lu ma mi ju vi sá  do lu ma mi ju vi sá  do lu ma mi ju vi sá"

        # Recojo la información de los meses: número de mes; días del mes; día de la semana en el que empieza el primer día del mes. 
        informacion_todos_meses=informacion_de_Meses()
        meses_completos=[]
        #Añado a la matriz de calendario anual los calendarios mensuales
        for i in range(12):
            meses_completos.append(crear_calendario_un_mes(primerDiaMes=informacion_todos_meses[i][2], num_dias=informacion_todos_meses[i][1], month=(i+1), year=anyoDado))
        # Printeo
        def printearMeses(indiceMes):
            print(crearEncabezadoMeses(indiceMes))
            print(DIASEMANA)
            #Poner aquí para ver cuál es el mes más largo, y elegir ese para poner "len" o aumentar el tamaño de los espacios en los meses.
            for i in range (6):
                print(meses_completos[indiceMes][i][0]+"  "+meses_completos[indiceMes+1][i][0]+"  "+meses_completos[indiceMes+2][i][0])

        print(encabezadoAnyo)
        printearMeses(indiceMes=0)
        printearMeses(indiceMes=3)
        printearMeses(indiceMes=6)
        printearMeses(indiceMes=9)
    # --------------- Reimpresión ---------------  
    print("_"*60)
    print("\n")
    print("Programa de impresión de calendarios. ")
    print("(Este programa es una práctica de matrices con programación modular en python)")
    print("a. Ver calendario de un mes y año concretos.")
    print("b. Ver calendario de un año.")
    print("c. Salir.")
    # Validar la opción del menú
    opcion = input("Elige una opción (a, b o c): ").strip().lower()

    while opcion not in ['a', 'b', 'c']:
        opcion = input("Opción incorrecta. Elige 'a' para calendario de mes y año, 'b' para calendario de año y 'c' para salir: ").strip().lower()
    # Si elige la opción 'b' (ver calendario de un mes y año concretos)
print("¡Que tenga un buen día!")













