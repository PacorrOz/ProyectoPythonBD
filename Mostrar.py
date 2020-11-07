from Conexion import Conexion

class Mostrar:
    
    def Mostrar(self):

        Conexion.mycursor = Conexion.mydb.cursor(buffered=True)
        Conexion.mycursor.execute('SELECT * FROM Alumno')

        if Conexion.mycursor.rowcount < 1:
            print(".::No hay registros para mostrar::.")
            return False
        else:
            for row in Conexion.mycursor:
                print(row)
            return True
