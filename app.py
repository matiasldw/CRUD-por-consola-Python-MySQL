from utils import funciones, valid_Crud
from Database import connection


def menu() -> int:
    print(funciones.separador('Menu'))
    print("1.- Listar cliente")
    print("2.- Registrar cliente")
    print("3.- Actualizar cliente")
    print("4.- Eliminar cliente")
    print("5.- Salir")
    print(funciones.separador())

    option = input('Seleccione una opción: ')

    return funciones.validador_option(option)


def action(valor: int):
    db = connection.Db()
    print()
    if valor == 1:
        try:
            result = db.getClientes()
            if result:
                valid_Crud.clientesList(result)
            else:
                print('No se encontraron clientes...')
        except Exception as ex:
            print(f'Ocurrió un error... ({ex})')
    elif valor == 2:
        try:
            cliente = valid_Crud.pedirDatos()
            db.createClient(cliente)
        except Exception as ex:
            print(f'Ocurrió un error... ({ex})')
    elif valor == 3:
        try:
            result = db.getClientes()
            if result:
                client_Update = valid_Crud.actualizarCliente(result)
                if client_Update is not None:
                    db.updateClient(client_Update)
                else:
                    print('El Id no existe...')
            else:
                print('No se encontraron clientes...')

        except Exception as ex:
            print(f'Ocurrió un error... ({ex})')
    elif valor == 4:
        try:
            result = db.getClientes()
            if result:
                client_Update = valid_Crud.borrarCliente(result)
                if client_Update is not None:
                    db.deleteClient(client_Update)
                else:
                    print('El Id no existe...')
            else:
                print('No se encontraron clientes...')

        except Exception as ex:
            print(f'Ocurrió un error... ({ex})')


if __name__ == '__main__':
    while True:
        election = menu()
        if election == 5:
            break
        action(election)
        print()
