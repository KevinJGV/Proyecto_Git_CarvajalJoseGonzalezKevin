import funciones_aux
import datos

ruta_json = "data.json"
registro = datos.traer_datos(ruta_json)

while True:
    funciones_aux.os.system("clear")
    funciones_aux.mensajes_consola("menu")
    op = funciones_aux.val_int(input("> "))
    if op < 1 or op > 4:
        funciones_aux.mensajes_consola("input")
    elif op == 1:
        funciones_aux.mensajes_consola("ver_registro", registro)