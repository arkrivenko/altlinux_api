import requests


class AltLinuxAPI:

    def __init__(self, endpoint='https://rdb.altlinux.org/api/'):
        self.endpoint = endpoint

    def export_branch_binary_packages(self, branch):
        url = f'{self.endpoint}/export/branch_binary_packages/{branch}'
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f'Ошибка запроса: {response.status_code}')
            return
