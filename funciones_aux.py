import os

# Limpiar la consola
os.system("clear")

def val_int(valor):
    while True:
        try:
            entrada = int(valor)
            return entrada
        except Exception as e:
            mensajes_consola("input")

def val_str(valor):
    while True:
        entrada = None
        try:
            entrada = int(valor)
            mensajes_consola("input")
        except Exception as e:
            return entrada

def mensajes_consola(op):
    if op == "input":
        input("Opción incorrecta, ingrese un valor/opción correctas.\n[Enter - Continuar]")
    elif op == "menu":
        print("=" * 5 + " GESTOR DE CIUDADES - KRUSTY KRAB V0.1 " + "=" * 5 + "\n1 - Visilizar ciudades\n2 - Registrar ciudad\n3 - Modificar registro\n4 - Salir de Krusty Krab")

def paginacion(structure_to_print, header, data_in_kwargs):
    start = 0
    pag_size = 5
    while True:
        end = start + pag_size
        print(header)
        if end > len(structure_to_print):
            end = len(structure_to_print)
        if start < 0:
            start = 0
        seccion = structure_to_print[start:end]
        current_page = ""
        for componente in seccion:
            line = ""
            if isinstance(structure_to_print,dict):
                line = " | ".join(list(componente.values())) + "\n"
            else:
                line = "".join(componente)
            current_page += line
        print(current_page)
        print(
            f"\t< {start} / {end} >\n[0 - Pagina anterior]    [1 - Pagina siguiente]\n[2 - Volver]")
        movimiento = int_val("> ", data_in_kwargs)
        if movimiento == 2:
            break
        elif movimiento == 1:
            start += pag_size
            if start > end:
                start -= pag_size
        elif movimiento == 0:
            if start != 0:
                start -= pag_size



