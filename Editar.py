from Conexion import Conexion

class Editar:

    def validaID(self, id):

        query = 'select * from Alumno where idAlumno=%s'
        Conexion.mycursor.execute(query, (id,))

        if Conexion.mycursor.rowcount < 1:
            print(".::No se encontro ese ID::.")
            return False
        else:
            return True
    
    def editaNombre(self, nombre, id):
        
        query = 'update Alumno set nombre=%s where idAlumno=%s'
        Conexion.mycursor.execute(query, (nombre, id,))
        Conexion.mydb.commit()
    
    def editaFecha(self, fecha, id):

        query = 'update Alumno set fecha=%s where idAlumno=%s'
        Conexion.mycursor.execute(query, (fecha, id,))
        Conexion.mydb.commit()
    
    def editaCalificacion(self, calificacion, id):
        
        query = 'update Alumno set calificacion=%s where idAlumno=%s'
        Conexion.mycursor.execute(query, (calificacion, id,))
        Conexion.mydb.commit()
    


    

