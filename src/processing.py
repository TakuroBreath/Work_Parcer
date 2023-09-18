import requests

from src.models.vacancy import Vacancy
from src.abstract_classes.apiwork import ApiWork

API_KEY = "v3.r.137828535.a18e6b0d7e5dfc1cfe9710f56cd30029b88d9d34.35bd02c4bed12991fc303bd1f26aea79631f801b"


class HeadHunter(ApiWork):
    """
    Implementation of the ApiWork class for interacting with the HeadHunter job vacancies API.
    """

    def __init__(self):
        """
        Initializes the HeadHunter API instance.
        Initializes the base URL for the HeadHunter API.
        """
        self._base_url = 'https://api.hh.ru/'

        def get_vacancies(self, name: str, salary: int = None, quantity: int = None) -> dict:
            """
            Fetches job vacancies from the HeadHunter API.

            :param name: Name of the job vacancy.
            :param salary: Desired salary for the vacancy.
            :param quantity: Number of vacancies to retrieve.
            :return: Dictionary containing job vacancy data.
            """

            url = f'{self._base_url}vacancies'
            headers = {
                'User-Agent': 'MyApp/job_parser maxsmurffy@gmail.com'
            }
            params = {
                'text': f'name:{name}',
                'salary': salary,
                'per_page': quantity,
            }

            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                data = response.json()
                return data
            elif response.status_code == 400:
                print('bad request')
            elif response.status_code == 403:
                print('access forbidden')
            elif response.status_code == 404:
                print('not found')
            else:
                print('unknown error')

        def parse(self, data: dict) -> list[Vacancy]:
            """
            Parses raw job vacancy data from the HeadHunter API.

            :param data: Raw data from the API.
            :return: List of parsed and structured Vacancy objects.
            """

            vacancies = []

            for el in data['items']:
                salary_data = el['salary']
                salary_from = salary_data.get('from') if salary_data else None
                salary_to = salary_data.get('to') if salary_data else None

                vac = Vacancy(title=el['name'],
                              vacancy_url=el['alternate_url'],
                              salary_from=salary_from,
                              salary_to=salary_to,
                              employer=el['employer']['name'],
                              city=el['area']['name'],
                              requirements=el['snippet']['requirement']
                              )

                vacancies.append(vac)
            return vacancies

    class SuperJobAPI(ApiWork):
        """
        Implementation of the ApiWork class for interacting with the SuperJob job vacancies API.
        """

        def __init__(self) -> None:
            """
            Initializes the Super Job API instance.
            Initializes the base URL for the SuperJob API.
            """
            self._base_url = 'https://api.superjob.ru/2.0/'

        def get_vacancies(self, name: str, salary: int = None, quantity: int = None) -> dict:
            """
            Fetches job vacancies from the SuperJob API.

            :param name: Name of the job vacancy.
            :param salary: Desired salary for the vacancy.
            :param quantity: Number of vacancies to retrieve.
            :return: Dictionary containing job vacancy data.
            """

            url = f'{self._base_url}vacancies'
            headers = {
                "X-Api-App-Id": API_KEY
            }
            params = {
                'keyword': name,
                'payment_from': salary,
                'count': quantity
            }

            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                data = response.json()
                return data
            elif response.status_code == 400:
                print('Bad Request')
            elif response.status_code == 403:
                print('Access Denied')
            elif response.status_code == 404:
                print('Not Found')
            else:
                print('Unknown Error')

        def parse(self, data: dict) -> list[Vacancy]:
            """
            Parses raw job vacancy data from the SuperJob API.

            :param data: Raw data from the API.
            :return: List of parsed and structured Vacancy objects.
            """

            vacancies = []

            for el in data['objects']:
                vac = Vacancy(title=el['profession'],
                              vacancy_url=el['link'],
                              salary_from=el['payment_from'],
                              salary_to=el['payment_to'],
                              employer=el['firm_name'],
                              city=el['client']['town']['title'],
                              requirements=el['vacancyRichText']
                              )

                vacancies.append(vac)
            return vacancies
