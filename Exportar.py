from Conexion import Conexion
from prettytable import from_db_cursor

class Exportar:

    def Exportar(self):
        
        Conexion.mycursor = Conexion.mydb.cursor(buffered=True)
        Conexion.mycursor.execute('SELECT * FROM Alumno')

        if Conexion.mycursor.rowcount > 0:

            tabla = from_db_cursor(Conexion.mycursor)
            f = open("datos.txt", "w+")
            f.write(tabla.get_string()) 
            f.close()

            input("\nDocumento creado")
        else:
            input("\n No hay datos para exportar")

"""
from Conexion import Conexion
from prettytable import from_db_cursor

class Exportar:
    def Exportar(self):
        Conexion.mycursor.execute('SELECT * FROM Alumno')

        if Conexion.mycursor.rowcount < 1:
            print(".::No hay registros para mostrar::.")
        else:

            tabla = from_db_cursor(Conexion.mycursor)
            f = open("datos.txt", "w+")
            f.write(tabla.get_string())
            f.close()
            input("\nDocumento creado")
"""