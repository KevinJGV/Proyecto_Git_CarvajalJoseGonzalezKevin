import json

def traer_datos(archivo):
    with open(archivo,"r", encoding="utf-8") as file:
        datos=json.load(file)
        return datos

def guardar_datos(datos,archivo):
    datos=json.dumps(datos,indent=3)
    with open(archivo,"w") as file:
        file.write(datos)
