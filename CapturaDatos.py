import datetime

class CapturaDatos:

    @staticmethod
    def leeCalificacion(message):
        calificacion = 0
        while True:
            try:
                calificacion = int(input(message))
                if calificacion < 0:
                    print('Error :: El número ingresado no debe ser negativo.')
                    continue
                if calificacion > 10:
                    print('Error :: Calificacion no debe ser mayor de 10.')
                    continue
                break
            except ValueError:
                print('Error :: El valor ingresado no corresponde a un número.')
        return calificacion

    @staticmethod
    def leeNombre(message):
        while True:
            texto = input(message)
            if all(x.isalpha() or x.isspace() for x in texto):
            #if texto.isalpha():
                if len(texto) < 5:
                    print("Error :: Nombre debe ser al menos 5 letras")
                
                elif len(texto) >= 100:
                    print("Error :: Ese nombre es muy largo, maximo 100 letras")
                else:
                    return texto
            else:
                print("Error :: Ah ingresado caracteres no validos")

    @staticmethod
    def leeFecha(message):
        while True:
            fecha = input(message)
            try:
                fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d')
                break
            except ValueError:
                print ("Debe ingresar la fecha con el formato aaaa-mm-dd: ")
        return fecha