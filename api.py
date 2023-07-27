import requests


class AltLinuxAPI:

    def __init__(self, endpoint='https://rdb.altlinux.org/api/'):
        self.endpoint = endpoint

    def export_branch_binary_packages(self, branch):
        response_result = []
        url = f'{self.endpoint}/export/branch_binary_packages/{branch}'
        try:
            response = requests.get(url)

            response_result = response.json().get('packages')
        except Exception as ex:
            print(f'An error occurred while executing the request: {ex}')
        finally:
            return response_result

    def get_all_pkgset_archs(self, branch):
        archs_list = []
        url = f'{self.endpoint}/site/all_pkgset_archs?branch={branch}'
        try:
            response = requests.get(url)

            archs_list = [arch.get('arch') for arch in response.json().get('archs')]
        except Exception as ex:
            print(f'An error occurred while executing the request: {ex}')
        finally:
            return archs_list
