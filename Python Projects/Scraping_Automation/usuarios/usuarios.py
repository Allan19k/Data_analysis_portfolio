import requests
import threading

def get_name():
    response = requests.get('https://randomuser.me/api/') 
    if response.status_code == 200:     
        results = response.json().get('results') 
        user = results[0]
        name = user.get('name').get('first') 
        email = user.get('email')
        username = user.get('login').get('username')
        password = user.get('login').get('password')
        picture = user.get('picture').get('large')
        print(f"Name: {name}, Email: {email}, Username: {username}, Password: {password}, Picture: {picture}")
    else:
        print(response.status_code)

if __name__ == '__main__': 
    for _ in range(10):  
        thread = threading.Thread(target=get_name)
        thread.start()
        thread.join()