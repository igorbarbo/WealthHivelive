from database.crud import create_client, get_client_portfolios

def add_new_client(name, age):
    client = create_client(name, age)
    return client

def list_client_portfolios(client_id):
    portfolios = get_client_portfolios(client_id)
    return portfolios
