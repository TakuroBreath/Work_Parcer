from src.processing import HeadHunter, SuperJob
from src.save_file import JsonSaver
import os

# The path to save files with vacancies
file_path_json = '../saved_vacancies/json_vacancies.json'


def search_vacancy():
    """Function for getting vacancies from platforms"""

    platforms = ['HeadHunter', 'SuperJob']
    hh_site = HeadHunter()
    sj_site = SuperJob()
    print(f'Available platforms: {platforms}')

    input_platform = int(input(f'Choose a platform: 1 - HeadHunter, 2 - SuperJob, 3 - HeadHunter and SuperJob: \n'))

    if input_platform not in [1, 2, 3]:
        print("Incorrect choice of platform.")
        return

    name = input("Enter the job title: ")
    salary = int(input("Enter the minimum salary in RUB: "))
    count = int(input("Enter the number of vacancies to search: "))

    hh_vacancies = []
    sj_vacancies = []

    if input_platform in [1, 3]:
        vacancies = hh_site.get_vacancies(name, salary, count)
        hh_vacancies = hh_site.parse(vacancies)

    if input_platform in [2, 3]:
        vacancies = sj_site.get_vacancies(name, salary, count)
        sj_vacancies = sj_site.parse(vacancies)

    all_vacancies = hh_vacancies + sj_vacancies
    if len(all_vacancies) > 0:
        print('Job search completed successfully')
    else:
        print('Job search failed, try changing the request parameters')
    return all_vacancies


def save_vacancies(vacancies):
    """Function for saving vacancies to a file"""
    json_save = JsonSaver(vacancies, f'../saved_vacancies/json_vacancies.json')
    json_save.save_to_file()
    print(f'the file was successfully saved along the path: ../job_parser/saved_vacancies/')


def remove_vacancies(vacancies):
    """Function for deleting a vacancy from a file"""

    json_save = JsonSaver(vacancies, f'../saved_vacancies/json_vacancies.json')

    remove_vac = input('Enter the exact name of the vacancy to delete: ')

    if os.path.isfile(file_path_json):
        json_save.delete_vacancy(remove_vac)
        print('the vacancy was successfully deleted from the JSON file')
    else:
        print('There is no file with vacancies')


def get_vac_by_salary(vacancies):
    """Function for getting a vacancy based on salary"""

    json_save = JsonSaver(vacancies, f'../saved_vacancies/json_vacancies.json')

    vac_by_sal = int(input('Enter salary to get vacancies: '))

    if os.path.isfile(file_path_json):
        vac_sal = json_save.get_vacancies_by_salary(vac_by_sal)
        for vac in vac_sal:
            print(vac)
    else:
        print('There is no file with vacancies')


def get_vac_by_city(vacancies):
    """Function for getting a vacancy based on the city"""

    json_save = JsonSaver(vacancies, f'../saved_vacancies/json_vacancies.json')

    vac_by_city = input('Enter the name city to get vacancies: ')

    if os.path.isfile(file_path_json):
        vac_city = json_save.get_vacancies_by_city(vac_by_city)
        for vac in vac_city:
            print(vac)
    else:
        print('There is no file with vacancies')


def get_top_vac(vacancies):
    """Function for getting top 3 vacancies"""

    json_save = JsonSaver(vacancies, f'../saved_vacancies/json_vacancies.json')

    if os.path.isfile(file_path_json):
        vac_top = json_save.top_vacancies(3)
        return vac_top
    #     for vac in vac_top:
    #         print(vac)
    # else:
    #     print('There is no file with vacancies')


def get_all_vacancies(vacancies):
    """Function for getting all vacancies"""

    json_save = JsonSaver(vacancies, f'../saved_vacancies/json_vacancies.json')

    if os.path.isfile(file_path_json):
        vac_all = json_save.load_from_file()
        for vac in vac_all:
            print(vac)
    else:
        print('There is no file with vacancies')
