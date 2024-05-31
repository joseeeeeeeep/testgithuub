menu=["Cafe"]
salir=True
opcion=0;

def mostrar():
    for item in menu:
        print(item)

def agregar(cafe):
    try:
        menu.append(cafe)
        return 1
    except ValueError as error:
        print("Problemas al agregar")

def insertar(posicion, cafe):
    try:
        menu.insert(posicion,cafe)
        return 1
    except ValueError as error:
        print("PRoblemas al insertar")

def eliminar(cafe):
    try:
        menu.remove(cafe)
        return 1
    except ValueError as error:
        print("No se elimino")

def actualizar(cafe_viejo, cafe_nuevo):
    try:
        retorno=0
        menu.remove(cafe_viejo)
        retorno=1
        menu.append(cafe_nuevo)#OJO
        retorno=2
        return retorno
    except ValueError as error:
        print("Problemas al actualizar el cafe, vea que este en la lista")
try:
    while salir:
        print("MENU")
        print("Administrar el cafe")
        print("1)Agregar")
        print("2)Mostrar")
        print("3)Eliminar")
        print("4)Modificar")
        print("5)Salir")
        opcion=int(input("Seleccione una opcion del 1 al 5\n"))
        if(opcion==1):
            aux=input("Ingrese nombre del cafe")
            if agregar(aux)==1:
                print("Agrego Correctamente")
        elif opcion==2:
            mostrar()
        elif opcion==3:
            print("A continuacioo se muestran los cafes agregados")
            mostrar()
            ayuya=input("Ingrese el cafe a eliminar\n")
            if eliminar(ayuya)==1:
                print("Elimino correctamente")
        elif opcion==4:
            print("A continuacioo se muestran los cafes agregados")
            mostrar()
            ayuya=input("Ingrese el cafe a modificar\n")
            ayuyita=input("Ingrese el nuevo cafe\n")
            aux=actualizar(ayuya, ayuyita)
            if aux==2:
                print("Se actualizo correctamente")
            elif(aux==1):
                print("PRoblemas al agregar el nuevo cafe")
            elif aux==0:
                print("Problemas al encontrar el cafe a actualizar")
        elif opcion==5:
            salir=False
except:
    print("Error inesperado, comuniquese al 800 360 360")