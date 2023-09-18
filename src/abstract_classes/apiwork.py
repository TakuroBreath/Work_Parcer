from abc import ABC, abstractmethod
import requests


class ApiWork(ABC):
    @abstractmethod
    def get_vacancies(self, name: str, salary: float, count: int) -> dict:
        """
        :param self:
        :param name: Name of the job
        :param salary: Salary of the job
        :param count: Count of the vacancies
        :return: Returns a dictionary with vacancies data
        """
        pass

    @abstractmethod
    def parse(self, data: dict) -> list:
        """

        :param self:
        :param data: Dictionary with data to parse
        :return: List of structured data about the job
        """
        pass
