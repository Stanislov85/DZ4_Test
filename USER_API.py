import requests

with open('token_ya.txt', 'r') as file_object:
    token_ya = file_object.read().strip()

url = 'https://cloud-api.yandex.net/v1/disk/resources'

def create_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': token_ya}
    create_dir = requests.api.put(url, headers=headers, params=params)
    return print(create_dir.status_code)

def delete_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': token_ya}
    create_dir = requests.api.delete(url, headers=headers, params=params)
    return create_dir.status_code

