import mysql.connector

class Mostrar:
    
    def Mostrar(self):

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port="3306",
            database="Escuela"
        )

        mycursor = mydb.cursor()

        mycursor.execute('SELECT * FROM Alumno')
        
        for row in mycursor:
            print(row)
