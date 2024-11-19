import requests


class HeadHunterApi:
    """Класс для апи hh.ru"""

    def __init__(self, companies):
        self.companies = companies
        self.url = "https://api.hh.ru/vacancies"
        self.params = {"employer_id": companies}
        self.vacancies = []

    def get_api(self):
        return requests.get(self.url, params=self.params)

    def get_vacan(self):
        response = self.get_api()
        if response.status_code == 200:
            data = response.json()
            vacan = data.get("items")
            self.vacan.append(vacan)
            return self.vacan
        else:
            return []
