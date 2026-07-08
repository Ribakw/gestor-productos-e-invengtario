import os
os.system('cls')

def menu():
    print('''========== MENÚ PRINCIPAL ==========
1. Stock por categoría
2. Buscar productos por rango de precio
3. Actualizar precio 
4. Agregar producto
5. Eliminar producto
6. Mostrar productos
7. Salir
===================================
''')

def valNombre(nombre):
    return nombre.strip().lower() != ""

def valCategoria(categoria):
    return categoria.strip().lower() != ""

def valPrecio(precio):
    return precio > 0

def valDisponible(disponible):
    return disponible.lower().strip() in ['s', 'n']

def leerOpcion(opcion):
    try:
        opcion = int(input("Ingrese una opción del 1 al 7: "))
        if opcion in range(1, 8):
            return opcion
        else:
            print("error. Debe ingresar una opción del 1 al 7")
    except ValueError:
        print("error. Debe ingresar una opción del 1 al 7")
    
