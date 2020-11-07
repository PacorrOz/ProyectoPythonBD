from Conexion import Conexion

class Exportar:
    def Exportar(self):
        Conexion.mycursor.execute('SELECT * FROM Alumno')

        f = open("datos.txt", "w+")
        for row in Conexion.mycursor:
            f.write(str(row))      
            f.write("\n")  
        f.close()

        input("\nDocumento creado")