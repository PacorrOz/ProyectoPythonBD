from Conexion import Conexion
class InsertaDatos:
    

    def Add(self,nombre, fecha, calificacion):
        
        query = 'INSERT INTO Alumno(nombre, fecha, calificacion) VALUES(%s, %s, %s)'
        Conexion.mycursor.execute(query, [nombre, fecha, calificacion])
        Conexion.mydb.commit()



    
