tamano = 5
verMenu = 1
operaciones = []
numero = int(input('Digite un numero para validar: '))
for i in range(tamano):
    if i == 0:
        operaciones.append('Finalizo')
    elif i == 1:
        if numero % 2 == 0: operaciones.append(f'El numero {numero} es multipo de 2')
        else: operaciones.append(f'El numero {numero} NO es multipo de 2')
    elif i == 2:
        raiz = pow(numero,1/2)
        operaciones.append(f'Raiz cuadrada de {numero} es: {raiz}')
    elif i == 3:
        operaciones.append(f'El numero {numero} sumado mas 100 es igual a {numero + 100}')
    elif i == 4:
        operaciones.append(f'El numero {numero} elavado es igual a {numero * numero}')

while verMenu == 1:
    opcion = int(input('\nQue desea hacer?\n'
                       '\nOPCION #0: Salir\n'
                        'OPCION #1: Encontar si el numero es multipo del 2\n'
                       'OPCION #2: Encontar raiz cuadrada\n'
                       'OPCION #3: Sumar 100 al numero ingresado\n'
                       'OPCION #4: Elevar el numero\n'))
    print(operaciones[opcion])
    if opcion == 0:
        break
    else:
        verMenu = int(input('Desea ver el menu nuevamente? Digite 1 para SI, 2 para NO: '))