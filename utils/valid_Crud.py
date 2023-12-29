from utils.funciones import separador, pedidoDeDatos


def clientesList(clients) -> None:
    print(separador('Clientes', 73))
    print(f'Id\t{"Nombre".ljust(15)}{"Apellido".ljust(15)}{"Dirección".ljust(30)}Teléfono')
    print('-'*73)

    for client in clients:
        client = list(client)
        if None in client:
            if client[3] is None:
                client[3] = ''
            if client[4] is None:
                client[4] = ''
        print(f'{client[0]}\t{client[1].ljust(15)}{client[2].ljust(15)}{client[3].ljust(30)}{client[4]}')


def pedirDatos() -> tuple:
    cliente = pedidoDeDatos()

    return cliente


def actualizarCliente(clients: tuple) -> list:
    clientesList(clients)

    id_Cliente = input('Elija Id del cliente a Actualizar: ')
    while not id_Cliente.isnumeric():
        id_Cliente = input('Reingrese Id del cliente a Actualizar: ')
    else:
        id_Cliente = int(id_Cliente)

    try:
        resultado = list(list(filter(lambda x: x[0] == id_Cliente, clients))[0])

        clienteUpdate = pedidoDeDatos()
        resultado[1] = clienteUpdate[0]
        resultado[2] = clienteUpdate[1]
        resultado[3] = clienteUpdate[2]
        resultado[4] = clienteUpdate[3]

        return resultado
    except:
        return None


def borrarCliente(clients: tuple) -> int:
    clientesList(clients)

    id_Cliente = input('Elija Id del cliente a Borrar: ')
    while not id_Cliente.isnumeric():
        id_Cliente = input('Reingrese Id del cliente a Borrar: ')
    else:
        id_Cliente = int(id_Cliente)
    try:
        resultado = list(list(filter(lambda x: x[0] == id_Cliente, clients))[0])
        return resultado[0]
    except:
        return None
