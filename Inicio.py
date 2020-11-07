import os
import InsertaDatos
import Editar
import Delete
import Mostrar
from CapturaDatos import CapturaDatos

C = CapturaDatos()
mostrar = Mostrar.Mostrar()

def menu():
    os.system('cls') #funcion que limpia la pantalla 
    print("Seleccione una opcion")
    print("\t1 - Agregar")
    print("\t2 - Actualizar")
    print("\t3 - Eliminar")
    print("\t4 - Mostrar")
    print("\t5 - Salir")

while True:
    menu()
    opcionMenu = input("-->> ")

    if opcionMenu == "1":

        nombre = C.leeNombre("Escribe el nombre del alumno: ")
        fecha = C.leeFecha("Ingresa la fecha en formato YYYY-MM-DD: ")
        calificaciones = C.leeCalificacion("Ingresa la calificacion: ")

        Addpersona = InsertaDatos.InsertaDatos()
        Addpersona.Add(nombre, fecha, calificaciones)
        input(".::Registro agregado exitosamente::.")
        
    elif opcionMenu == "2":
        
        print("Actualizar datos \t")
        mostrar.Mostrar()
        editar = Editar.Editar()

        id = int(input("¿Cual persona deseas editar?: "))

        print("¿Qué dato desea actualizar?")
        print("\t1 - Actualizar nombe")
        print("\t2 - Actualizar fecha")
        print("\t3 - Actualizar calificacion")
        opactualizar = input("Elija su opcion >> ")

        if opactualizar =="1":
            nombre = C.leeNombre("Ingrese el nuevo nombre de la persona: ")
            editar.editaNombre(nombre, id)
            input(".::El nombre de actulizo exitosamente::.")

        elif opactualizar == "2":
            fecha = C.leeFecha("Ingresa la nueva fecha: ")
            editar.editaFecha(fecha, id)
            input(".::La fecha se actualizo exitosamente::.")

        elif opactualizar =="3":
            calificacion = C.leeCalificacion("Ingresa la nueva calificacion: ")
            editar.editaCalificacion(calificacion, id)
            input(".::La fecha se actualizo exitosamente::.")

    elif opcionMenu == "3":
        
        print("Eliminar datos \t")

        mostrar.Mostrar()
        borrar = Delete.Delete()
        id = int(input("¿Cual persona deseas eliminar?: "))
        
        borrar.delete(id)
        input(".::Registro eliminado exitosamente::.")
 
    elif opcionMenu == "4":
        
        print("Mostrando Datos \t")
        mostrar.Mostrar()
        input("\npulsa una tecla para continuar")

    elif opcionMenu == "5":
        break
    else:
        print("")
        input("No has pulsado ninguna opcion correcta...\npulsa una tecla para continuar")
        