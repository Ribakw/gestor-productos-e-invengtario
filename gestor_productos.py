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
    
def validar_vendidos(vendidos):
    try:
        valor = int(vendidos)
        return valor >= 0
    except ValueError:
        return False

def leer_opcion():
    try:
        opcion = int(input("Seleccione una opción: "))
        if 1 <= opcion <= 7:
            return opcion
        else:
            return -1
    except ValueError:
        return -1

def menu():
    print('''========== MENÚ PRINCIPAL ==========
1. Stock por categoría
2. Buscar productos por rango de precio
3. Actualizar precio 
4. Agregar producto
5. Eliminar producto
6. Mostrar productos
7. Salir
===================================''')