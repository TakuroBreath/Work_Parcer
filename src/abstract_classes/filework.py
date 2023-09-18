from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def save_to_file(self):
        pass

    @abstractmethod
    def load_from_file(self):
        pass

    @abstractmethod
    def top_vacancies(self, number):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary):
        pass

    @abstractmethod
    def get_vacancies_by_city(self, city):
        pass

    @abstractmethod
    def delete_vacancy(self, criteria):
        pass
