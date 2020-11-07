from Conexion import Conexion

class Delete:

    def validaID(self, id):

        query = 'select * from Alumno where idAlumno=%s'
        Conexion.mycursor.execute(query, (id,))

        if Conexion.mycursor.rowcount < 1:
            print(".::No se encontro ese ID::.")
            return False
        else:
            return True
            
    def delete(self, id):
        
        query = 'DELETE from alumno where idAlumno=%s'
        Conexion.mycursor.execute(query, (id,))
        Conexion.mydb.commit()
