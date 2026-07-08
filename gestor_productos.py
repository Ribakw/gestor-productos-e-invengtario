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

