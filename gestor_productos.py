import os
os.system('cls') 

def validar_codigo(codigo, productos):                                  
    if not codigo or codigo.isspace():
        return False
    for x in productos.keys():
        if x.lower() == codigo.lower():
            return False
    return True

def validar_nombre(nombre):
    if not nombre or nombre.isspace():
        return False
    return True

def validar_categoria(categoria):
    if not categoria or categoria.isspace():
        return False
    return True

def validar_precio(precio):
    try:
        valor = int(precio)
        return valor > 0
    except ValueError:
        return False

def validar_disponible(opcion):
    if not opcion:
        return False
    return opcion.lower() in ['s', 'n']

def validar_stock(stock):
    try:
        valor = int(stock)
        return valor >= 0
    except ValueError:
        return False
    
    