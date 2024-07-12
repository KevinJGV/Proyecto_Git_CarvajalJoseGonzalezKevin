import funciones_aux
import datos

import modulo_ciudades 

ruta_json = "data.json"
registro = datos.traer_datos(ruta_json)

while True:
    funciones_aux.os.system("clear")
    funciones_aux.mensajes_consola("menu")
    op = funciones_aux.val_int(input("> "))
    if op < 1 or op > 3:
        funciones_aux.mensajes_consola("input")           
    elif op == 1:
        funciones_aux.mensajes_consola("ver_registro", registro)
    elif op==2:
        print("Deseas ingresar a: ")
        print("1- Modulo ciudades")
        print("2- Modulo Busqueda")
        opcion=input("Ingresa la opcion que deseas: ")
        if opcion=="1":
            modulo_ciudades.modulo_ciudades()
        elif opcion=="2":
            modulo_ciudades.buscar_ciudades(registro)
        else:
            print("Debias escoger una de las opciones dadas")
            