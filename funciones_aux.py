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
            os.system("clear")

def val_str(valor):
    while True:
        entrada = None
        try:
            entrada = int(valor)
            mensajes_consola("input")
            os.system("clear")
        except Exception as e:
            return entrada

def mensajes_consola(op, extra=None):
    if op == "input":
        input("Opción incorrecta, ingrese un valor/opción correctas.\n[Enter - Continuar]\n>")
    elif op == "menu":
        print("=" * 5 + " GESTOR DE CIUDADES - KRUSTY KRAB V0.1 " + "=" * 5 + "\n1 - Visualizar Ciudades\n2 - CRUD al registro\n3 - Salir de Krusty Krab")
    elif op == "ciudades":
        print("> PENDIENTE" + "\n1 - Visilizar ciudades\n2 - Registrar ciudad\n3 - Modificar registro\n4 - Salir de Krusty Krab")
    elif op == "ver_registro":
        ver_registro(extra)


def ver_registro(registro):
    keys = [key for key in registro[0]]
    header = " | ".join(keys).upper() + "\n"
    start = 0
    pag_size = 5
    while True:
        os.system("clear")
        print("> Visualizar Ciudades")
        end = start + pag_size
        print(header)
        if end > len(registro):
            end = len(registro)
        if start < 0:
            start = 0
        seccion = registro[start:end]
        current_page = ""
        for ciudad in seccion:
            line = ""
            values = list(ciudad.values())
            fixed_values = []
            for i in values:
                fixed_values.append(str(i))
            line = " | ".join(fixed_values) + "\n"
            current_page += line
        print(current_page)
        print(
            f"\t\t< {start} / {end} >\n[0 - Pagina anterior]    [1 - Pagina siguiente]\n[2 - Volver]")
        movimiento = val_int(input("> "))
        if movimiento == 2:
            break
        elif movimiento == 1:
            start += pag_size
            if start > end:
                start -= pag_size
        elif movimiento == 0:
            if start != 0:
                start -= pag_size



