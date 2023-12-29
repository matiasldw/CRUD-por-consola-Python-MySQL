from mysql.connector import connection, Error
from dotenv import load_dotenv
import os

load_dotenv()


class Db:

    def __init__(self):
        user = os.getenv('DB_USERNAME')
        host = os.getenv('DB_HOST')
        passw = os.getenv('DB_PASSWORD')
        db = os.getenv('DB_DATABASE')

        config = {
            'host': host,
            'user': user,
            'password': passw,
            'database': db
        }
        try:
            self.db_connection = connection.MySQLConnection(**config)
        except Error as ex:
            print(f"Error al intentar la conexión: {ex}")

    def getClientes(self):
        if self.db_connection.is_connected():
            try:
                with self.db_connection.cursor() as cursor:
                    # cursor.execute('SELECT * FROM clientes')
                    cursor.callproc('SP_Listar')
                    result = cursor.stored_results()
                    return next(result).fetchall()
            except Error as ex:
                print(f'Error al intentar la conexion... ({ex})')

    def createClient(self, client: tuple):
        if self.db_connection.is_connected():
            try:
                with self.db_connection.cursor() as cursor:
                    cursor.callproc('SP_Guardar', client)
                    self.db_connection.commit()
                    print('¡¡¡ Cliente Registrado Ok !!!')
            except Error as ex:
                print(f'Error al intentar la conexion... ({ex})')

    def updateClient(self, client: list):
        if self.db_connection.is_connected():
            try:
                with self.db_connection.cursor() as cursor:
                    cursor.callproc('SP_Editar', client)
                    self.db_connection.commit()
                    print('¡¡¡ Cliente Actualizado Ok !!!')
            except Error as ex:
                print(f'Error al intentar la conexion... ({ex})')

    def deleteClient(self, id_Cliente: int):
        if self.db_connection.is_connected():
            try:
                with self.db_connection.cursor() as cursor:
                    cursor.callproc('SP_Eliminar', (id_Cliente,))
                    self.db_connection.commit()
                    print('¡¡¡ Cliente Borrado Ok !!!')
            except Error as ex:
                print(f'Error al intentar la conexion... ({ex})')
