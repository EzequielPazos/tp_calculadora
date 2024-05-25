def mostrar_menu_calculadora(primer_operando:float,segundo_operando:float)->None:
    """muestra un menu personalizado

    Args:
        primer_operando (float): 1er operando cargado en el sistema
        segundo_operando (float): 2do operando cargado en el sistema

    Returns:
        None
    """

    print (f"""
    ┌───────────────────────────────────┐ 
    │                                   │  
    │   CALCULADORA       __________    │
    │                    | ________ |   │
    │     "KSIO"         ||12345678||   │
    │                    |----------|   │
    │                    |[M|#|C][-]|   │
    │                    |[7|8|9][+]|   │
    │                    |[4|5|6][x]|   │
    │                    |[1|2|3][%]|   │
    │                    |[.|O|:][=]|   │
    │                    "----------"   │                                   
    └───────────────────────────────────┘ 
        
    [1]Ingresar el primer operando (A = {primer_operando})
    [2]Ingresar el segundo operando (B = {segundo_operando})
    [3]Calcular todas las operaciones
    [4]Informar resultados
    [5]Salir del programa
    """)

def validar_entero(entrada)->int:
    """valida que el numero dado por entrada sea un entero

    Args:
        entrada (_type_): elemento a testear

    Returns:
        int: entrada validada que sea un numero entero
    """
    while True:
        try:
            entrada_validada = int(entrada)
            break #salgo del while
        except ValueError: #si la opcion ingresada no es type int da ValueError
            entrada = input("Por favor ingrese un numero entero! Ingreso: ")
            continue
    return entrada_validada

def pedir_opcion_numerica(cantidad_opciones:int)->int:
    """pide una opcion numerica y la valida

    Args:
        cantidad_opciones (int): cantidad de opciones a elegir

    Returns:
        int: opcion elegida y validada
    """
    
    opcion_ingresada = validar_entero(input("\nIngrese la opcion deseada: "))
    
    while True:
        if opcion_ingresada not in range(1,cantidad_opciones+1):
            opcion_ingresada = validar_entero(input("Ingrese una opcion dentro del rango! Seleccion: "))
            continue
        else:
            break
        
    return opcion_ingresada

def validar_numero(entrada)->float:
    """valida que la entrada dada sea un numero

    Args:
        entrada (_type_): entrada a testear

    Returns:
        float: devuelve la entrada si es un numero
    """
    while True:
        try:
            entrada_validada = float(entrada)
            break #salgo del while
        except ValueError: #si la opcion ingresada no es type float da ValueError
            entrada = input("Por favor ingrese un numero! Ingreso: ")
            continue
    return entrada_validada

def sumar_dos_numeros(primer_numero:float,segundo_numero:float)->float:
    """suma dos numeros

    Args:
        primer_numero (float): primer numero
        segundo_numero (float): segundo numero

    Returns:
        float: suma de los numeros
    """
    return primer_numero + segundo_numero

def restar_dos_numeros(primer_numero:float,segundo_numero:float)->float:
    """resta dos numeros

    Args:
        primer_numero (float): primer numero
        segundo_numero (float): segundo numero

    Returns:
        float: resta de los numeros
    """
    return primer_numero - segundo_numero

def dividir_dos_numeros(primer_numero:float,segundo_numero:float)->float:
    """divide dos numeros

    Args:
        primer_numero (float): primer numero
        segundo_numero (float): segundo numero

    Returns:
        float: resultado de la division si fue hecha
    
    Raises:    
        ZeroDivisionError: si se intento dividir por 0
    """
    if segundo_numero == 0:
        raise ZeroDivisionError
    
    return primer_numero / segundo_numero
    
def multiplicar_dos_numeros(primer_numero:float,segundo_numero:float)->float:
    """multiplica dos numeros

    Args:
        primer_numero (float): primer numero
        segundo_numero (float): segundo numero

    Returns:
        float: multiplicacion de los numeros
    """
    return primer_numero * segundo_numero

def factorial_numero_entero(numero:int)->int:
    """factoriza un numero entero de manera recursiva

    Args:
        numero (int): numero a factorizar

    Returns:
        int: factoreo del numero
        0: si se intenta factorizar por 0 o por un numero decimal
        1: si el numero a factorizar es 0 o 1
    """
    if numero < 0 or numero%1 !=0:
        return 0
    elif numero == 0:
        return 1
    elif numero == 1:
        return numero
    else:
        return numero*factorial_numero_entero(numero-1)

