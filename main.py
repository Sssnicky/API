from pprint import pprint
import requests
import datetime
import time
# ЗАДАНИЕ НОМЕР 1


def test_request():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url=url)
    superheroes = {}
    for i in response.json():
        if i['name'] == 'Hulk' or i['name'] == 'Captain America' or i['name'] == 'Thanos':
            superheroes[i['name']] = i['powerstats']['intelligence']
    if superheroes['Captain America'] > superheroes['Hulk'] and superheroes['Captain America'] > superheroes['Thanos']:
        return 'Captain America is the most intelligent superhero'
    elif superheroes['Hulk'] > superheroes['Captain America'] and superheroes['Hulk'] > superheroes['Thanos']:
        return 'Hulk is the most intelligent superhero'
    else:
        return 'Thanos is the most intelligent superhero'


if __name__ == '__main__':
    print(test_request())


# ЗАДАНИЕ НОМЕР 2
class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, filename, disk_file_path):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return "Success"


if __name__ == '__main__':
    path_to_file = 'text.txt'
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, "netology/test.txt")

# ЗАДАНИЕ НОМЕР 3


def get_questions_python_last_2_days():
    url = 'https://api.stackexchange.com/2.3/questions?'
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    date = datetime.datetime(year, month, day)
    unix_date_today = int(time.mktime(date.timetuple()))
    yesterdate = datetime.datetime(year, month, day - 1)
    unix_date_yesterday = int(time.mktime(yesterdate.timetuple()))
    url += f'fromdate={unix_date_yesterday}&todate={unix_date_today}&tagged=python&site=stackoverflow'
    print(url)
    res = requests.get(url=url).json()
    return res


res = get_questions_python_last_2_days()
pprint(res)






