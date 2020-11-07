from Conexion import Conexion

class Editar:
    
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
    


    

