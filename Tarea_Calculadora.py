import time

x=float(input('\nIngrese su primer número: '))
y=float(input('Ingrese su segundo numero: '))

opc=0
inicio=time.time()
while opc!=5:
    print('''\n
********************************************* 
           
    Calculadora básica
----1. Suma----------------------------------
----2. Resta---------------------------------
----3. Multiplicación------------------------
----4. División------------------------------
----5. Salir---------------------------------
          
*********************************************''')
    print('\nSeleccione el número de la operacion que desea realizar: ')
    opc=int(input())

    if opc==1:
        suma=x+y
        print('\nEl resultado es:', suma)
        fin = time.time()
        tiempo_ejecutado = fin - inicio
        print('Tiempo en ejecutar la suma: ',tiempo_ejecutado)

    if opc==2:
        resta=x-y
        print('\nEl resultado es:', resta)
        fin = time.time()
        tiempo_ejecutado = fin - inicio
        print('Tiempo en ejecutar la resta: ',tiempo_ejecutado)

    if opc==3:
        multiplicacion=x*y
        print('\nEl resultado es:', multiplicacion)
        fin = time.time()
        tiempo_ejecutado = fin - inicio
        print('Tiempo en ejecutar la multiplicación: ',tiempo_ejecutado)

    if opc==4:
        division=x/y
        print('\nEl resultado es:', division)
        fin = time.time()
        tiempo_ejecutado = fin - inicio
        print('Tiempo tardado en ejecutar la división: ',tiempo_ejecutado)
        
    if opc==5:
        print('\nHasta luego amiguito, vuelva pronto...!!!!')