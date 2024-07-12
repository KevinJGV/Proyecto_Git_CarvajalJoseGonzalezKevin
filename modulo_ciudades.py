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
        modificar_ciudad(datos_ciudades)
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
    
def modificar_ciudad(datos_ciudades):
    lista_ciudades=[]
    numero_ciudad=1
    print("Las ciudades guardadas son: ")
    for i in datos_ciudades:
        lista_ciudades.append(i["nombre"])
        print(f"{numero_ciudad}- "+str(i["nombre"]))
        numero_ciudad+=1
    
    ciudad_nombre=int(input("Ingrese el numero de la ciudad que desea modificar\n >> "))
    ciudad_nombre=lista_ciudades[ciudad_nombre-1]
    
    print("\nLos datos que se tienen de las ciudades son:")
    print("1- Nombre")
    print("2- Còdigo postal")
    print("3- Poblaciòn estimada")
    print("4- Paìs")
    lista_opciones=["nombre","codigo_postal","poblacion_estimada","pais"]
    opcion=int(input("Ingresa la opcion que desee modificar\n>> "))
    opcion=lista_opciones[opcion-1]
    
    for ciudad in datos_ciudades:
        if ciudad["nombre"]==ciudad_nombre:
            print(f"{ciudad_nombre} en el apartado {opcion} tiene actualmente un valor de: {ciudad[opcion]}")
            if opcion=="codigo_postal" or opcion=="poblacion_estimada":
                nuevo_valor=int(input("Ingrese el nuevo valor\n>> "))
            else:
                nuevo_valor=input("Ingrese el nuevo valor\n>> ")       
            ciudad[opcion]=nuevo_valor
            print("Modificacion realizada correctamente")
            guardar_datos(datos_ciudades,RUTA_CIUDADES)

def buscar_ciudades(datos_ciudades):
    print("Busqueda por:")
    print("1- Nombre")
    print("2- Pais")
    print("3- Codigo postal")
    lista_opciones=["nombre","pais","codigo_postal"]
    opcion=int(input("Ingrese el metodo de busqueda de ciudad que desea realizar\n>> "))
    opcion=lista_opciones[opcion-1]
    
    
    dato=input(f"Ingresa el {opcion} por el que deseas buscar\n>> ")

    print(f"*Ciudades con {opcion} igual a {dato}: ")
    encontrado=False
    for ciudad in datos_ciudades:
        try:
            dato=dato.lower()
            ciudad[opcion]=ciudad[opcion].lower()
        except:
            dato=int(dato)
        if ciudad[opcion] == dato:
            encontrado=True
            print("******************************")
            print("Nombre: "+ ciudad["nombre"])
            print("Codigo_postal: "+ str(ciudad["codigo_postal"]))
            print("Poblacion estimada: "+ str(ciudad["poblacion_estimada"]))
            print("Pais: "+ ciudad["pais"])
            print("******************************")
    
    if encontrado==False:
        print(f"No se encontro alguna ciudad con {opcion} que sea {dato}")

