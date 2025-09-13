import requests
import threading

def get_pokemon(response_json):
    name = response_json.get('forms')[0].get('name')
    print(f'El nombre del pokemon es : {name}')
    print(f'El peso del pokemon es : {response_json.get("weight")}')
    print(f'El tipo del pokemon es : {response_json.get("types")[0].get("type").get("name")}')
    print(f'El movimiento del pokemon es : {response_json.get("moves")[0].get("move").get("name")}')
    # dar salto de linea
    print()

def get_user(response_json):
    name = response_json.get('results')[0].get('name').get('first')
    print(f'El nombre del usuario es : {name}')

def error_request():
    print('Operación no exitosa')

def create_request(url, success_callback, error_callback):
    response = requests.get(url)
    if response.status_code == 200:
        success_callback(response.json())
    else:
        error_callback()

if __name__ == '__main__':
    t1 = threading.Thread(target=create_request, kwargs={
        'url': 'https://pokeapi.co/api/v2/pokemon/1/',
        'success_callback': get_pokemon,
        'error_callback': error_request
    })
    t2 = threading.Thread(target=create_request, kwargs={
        'url': 'https://randomuser.me/api',
        'success_callback': get_user,
        'error_callback': error_request
    })
    t3 = threading.Thread(target=create_request, kwargs={
        'url': 'https://pokeapi.co/api/v2/pokemon/2/',
        'success_callback': get_pokemon,
        'error_callback': error_request
    })
    t4 = threading.Thread(target=create_request, kwargs={
        'url': 'https://randomuser.me/api',
        'success_callback': get_user,
        'error_callback': error_request
    })
    t5 = threading.Thread(target=create_request, kwargs={
        'url': 'https://pokeapi.co/api/v2/pokemon/3/',
        'success_callback': get_pokemon,
        'error_callback': error_request
    })

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()