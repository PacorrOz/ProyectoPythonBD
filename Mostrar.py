from Conexion import Conexion
from prettytable import from_db_cursor

class Mostrar:
    
    def Mostrar(self):

        Conexion.mycursor = Conexion.mydb.cursor(buffered=True)
        Conexion.mycursor.execute('SELECT * FROM Alumno')

        if Conexion.mycursor.rowcount < 1:
            print(".::No hay registros para mostrar::.")
            return False
        else:

            tabla = from_db_cursor(Conexion.mycursor)
            #for row in Conexion.mycursor:
            print(tabla.get_string())
            return True
""" 
    INSTALACION PRETTYTABLE

    cd C:/Python38/
    pip install -U prettytable

"""