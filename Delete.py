from Conexion import Conexion

class Delete:

    def delete(self, id):
        
        query = 'DELETE from alumno where idAlumno=%s'
        Conexion.mycursor.execute(query, (id,))
        Conexion.mydb.commit()
