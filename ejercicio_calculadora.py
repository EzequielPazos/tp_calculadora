'''
Enunciado
Hacer una calculadora. Para ello el programa iniciará y contará con un menú de opciones:
1. Ingresar 1er operando (A=x)
2. Ingresar 2do operando (B=y)
3. Calcular todas las operaciones
a) Calcular la suma (A+B)
b) Calcular la resta (A-B)
c) Calcular la división(A/B)
d) Calcular la multiplicación(A*B)
e) Calcular factorial(A!)
4. Informar resultados
a) “El resultado de A+B es: r”
b) “El resultado de A-B es: r”
c) “El resultado de A/B es: r” o “No es posible dividir por cero”
d) “El resultado de A*B es: r”
e) “El factorial de A es: r1 y El factorial de B es: r2”
5. Salir
• Todas las funciones matemáticas del menú se deberán realizar en una biblioteca aparte,que contenga las funciones
para realizar las cinco operaciones.
• En el menú deberán aparecer los valores actuales cargados en los operandos A y B(donde dice “x” e “y” en el ejemplo,
se debe mostrar el número cargado)
• Deberán contemplarse los casos de error (división por cero, etc.)
• Documentar todas las funciones
'''

'''
DESENGLOBE DEL PROBLEMA

funcion menu
pedir opcion

1. ingresar el primer operando

ingreso numero y verifico cque sea un numero valido

2. ingresar el segundo operando

ingreso numero y  verifico que sea un numero valido

3. realizo las operaciones solo si se ingresaron ambos numeros
y si se pueden hacer
hacer funciones para cada operacion y que salve las excepciones

4. imprimir los resultados y si no se puede realizar que aclare

5.salir del programa

documentar todo
'''

'''
Alumno: Pazos Ezequiel
'''

import funciones_calculadora,os

primer_operando = 0  #  inicializo los operandos en 0 para indicar que aun no se ingreso ningun valor
segundo_operando = 0
CANT_OPCIONES_MENU = 5 
bandera_operaciones = 0  #  flag para saber si ya se realizaron las operaciones
bandera_division = 0  #  flag para saber si se dividio por 0 o no

while True:
    os.system('cls')
    funciones_calculadora.mostrar_menu_calculadora(primer_operando, segundo_operando)
    opcion_ingresada = funciones_calculadora.pedir_opcion_numerica(CANT_OPCIONES_MENU)
    match opcion_ingresada:
        case 1:  #  Ingresar el primer operando
            os.system('cls')
            primer_operando = funciones_calculadora.validar_numero(input("Ingrese el primer operando: "))
        case 2:  #  Ingresar el segundo operando
            os.system('cls')
            segundo_operando = funciones_calculadora.validar_numero(input("Ingrese el segundo operando: "))
        case 3:  #  Realizar operaciones
            os.system('cls')
            resultado_suma = funciones_calculadora.sumar_dos_numeros(primer_operando,segundo_operando)
            resultado_resta = funciones_calculadora.restar_dos_numeros(primer_operando,segundo_operando)
            resultado_multiplicacion = funciones_calculadora.multiplicar_dos_numeros(primer_operando,segundo_operando)
            try:
                resultado_division = funciones_calculadora.dividir_dos_numeros(primer_operando,segundo_operando)
                bandera_division = 1
            except ZeroDivisionError as e:
                bandera_division = 0
            resultado_factorial = funciones_calculadora.factorial_numero_entero(primer_operando)
            bandera_operaciones = 1
            input("\nOperaciones realizadas con exito! Presione Enter para continuar...")
        case 4:  #  Mostrar los resultados  
            os.system('cls')
            if not bandera_operaciones:
                input("\n No se pueden mostrar los resultados antes de realizar las operaciones! Presione Enter para continuar...")
            else:
                print(f"""
                --- RESULTADOS OPERACIONES ---

                OPERACION 1: SUMA

                {primer_operando} + {segundo_operando} = {resultado_suma}

                OPERACION 2: RESTA

                {primer_operando} - {segundo_operando} = {resultado_resta}
                            
                OPERACION 3: MULTIPLICACION

                {primer_operando} * {segundo_operando} = {resultado_multiplicacion}
                """)
                
                print("\nOPERACION 4: DIVISION")
                
                if not bandera_division:   
                    print(f"\n{primer_operando} / {segundo_operando} = No se puede dividir por 0! jaja")
                else:
                    print(f"\n{primer_operando} / {segundo_operando} = {resultado_division}")            
                
                print("\nOPERACION 5: FACTORIAL")
                
                if not resultado_factorial:
                    print(f"\n{primer_operando}! = No se puede realizar el factorial de numeros decimales ni menores a 0! Sry!")  
                else:
                    print(f"\n{primer_operando}! = {resultado_factorial}")
                    
                input("\nPresione Enter para continuar...")
        case 5:  #  Salgo del programa
            os.system('cls')
            print(f"""
             ____             ____             _ 
            |  _ \           |  _ \           | |
            | |_) |_   _  ___| |_) |_   _  ___| |
            |  _ <| | | |/ _ \  _ <| | | |/ _ \ |
            | |_) | |_| |  __/ |_) | |_| |  __/_|
            |____/ \__, |\___|____/ \__, |\___(_)
                    __/ |            __/ |       
                   |___/            |___/        """)       
            break