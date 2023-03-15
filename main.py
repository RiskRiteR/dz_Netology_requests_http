from pprint import pprint

import requests


def smartest_hero(list_name_hero: list):
    api_ = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    j_api = api_.json()
    list_hero = sorted([[_['powerstats']['intelligence'], _['name']] for _ in j_api if list_name_hero.count(_['name'])])
    return print(f'Самый умный супергерой {list_hero[-1][1]}')


smartest_hero(['Hulk', 'Captain America', 'Thanos'])
print()


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        url_to_load = data.get('href')
        return url_to_load

    def upload(self, disk_file_path, local_file_path):
        href = self.get_upload_link(disk_file_path=disk_file_path)
        response = requests.put(href, data=open(local_file_path, 'rb'))
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    local_path_to_file = input('Введите локальный адрес файла ')
    disk_path_to_file = input('Введите адрес куда загрузит файл ')
    TOKEN = input('Введите токен: ')
    uploader = YaUploader(token=TOKEN)
    uploader.upload(disk_path_to_file, local_path_to_file)


