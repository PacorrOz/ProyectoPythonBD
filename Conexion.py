class Conexion:
    import mysql.connector
    mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                port="3306",
                database="Escuela"
            )
    mycursor = mydb.cursor()