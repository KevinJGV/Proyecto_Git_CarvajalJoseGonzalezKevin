from datos import *

RUTA_CIUDADES="data.json"


def modulo_ciudades():
    datos_ciudades=traer_datos(RUTA_CIUDADES)
    print("1- Añadir ciudad")
    print("2- Editar ciudad")
    print("0- Salir")
    opcion=int(input("Ingresa la opcion que desee: \n>> "))
    if opcion==1:
        crear_ciudad(datos_ciudades)
    elif opcion==2:
        None
    elif opcion==0:
        return None
        
def crear_ciudad(datos_ciudades):

    print("De la ciudad a agregar ingresa los siguientes datos: \n")
    nombre=input("Nombre:   \n>> ")
    postal=int(input("Codigo postal:   \n>> "))
    poblacion=int(input("Poblacion estimada:   \n>> "))
    pais=input("Pais al que pertenece:   \n>> ")
    
    datos_ciudades.append("hola")
    datos_ciudades.append({"nombre":nombre,
                           "codigo_postal":postal,
                           "poblacion_estimada":poblacion,
                           "pais":pais})
    guardar_datos(datos_ciudades,RUTA_CIUDADES)
    
modulo_ciudades()