class Vacancy:
    """
    Represents a job vacancy with associated attributes and methods.

    Attributes:
        title (str): The title of the vacancy.
        vacancy_url (str): The URL link to the vacancy.
        salary_from (int, float, None): The minimum salary offered for the vacancy.
        salary_to (int, float, None): The maximum salary offered for the vacancy.
        employer (str): The name of the employer.
        city (str): The city where the vacancy is located.
        requirements (str): The requirements for the vacancy.
    """

    def __init__(self, title, vacancy_url, salary_from, salary_to, employer, city, requirements) -> None:
        """
        Initializes a Vacancy object.

        Args:
            title (str): The title of the vacancy.
            vacancy_url (str): The URL link to the vacancy.
            salary_from (int, float, None): The minimum salary offered for the vacancy.
            salary_to (int, float, None): The maximum salary offered for the vacancy.
            employer (str): The name of the employer.
            city (str): The city where the vacancy is located.
            requirements (str): The requirements for the vacancy.

        Raises:
            ValueError: If any of the provided attributes are of invalid type.
        """
        if not isinstance(title, str):
            raise ValueError("Title must be a non-empty string")
        if not isinstance(vacancy_url, str):
            raise ValueError("Vacancy URL must be a non-empty string")
        if not (isinstance(salary_from, (int, float, type(None))) and isinstance(salary_to, (int, float, type(None)))):
            raise ValueError("Salary values must be numeric or None")
        if not isinstance(employer, str):
            raise ValueError("Employer must must be a non-empty string")
        if not isinstance(city, str):
            raise ValueError("City must be a non-empty string")
        if not isinstance(requirements, str):
            raise ValueError("Requirements must be a non-empty string")

        self.title = title
        self.vacancy_url = vacancy_url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.employer = employer
        self.city = city
        self.requirements = requirements

        if salary_from is None or salary_to is None:
            self.salary_comparison = 0
        else:
            self.salary_comparison = (salary_from + salary_to) / 2

    def __getitem__(self, key):
        """
        Accesses the attributes of the Vacancy object using the [] operator.

        Args:
            key (str): The attribute key to access.
        Returns:
            The value of the specified attribute.
        Raises:
            KeyError: If the specified key is not a valid attribute of Vacancy.
        """
        if key == 'title':
            return self.title
        elif key == 'vacancy_url':
            return self.vacancy_url
        elif key == 'salary_from':
            return self.salary_from
        elif key == 'salary_to':
            return self.salary_to
        elif key == 'employer':
            return self.employer
        elif key == 'city':
            return self.city
        elif key == 'requirements':
            return self.requirements
        else:
            raise KeyError(f"'{key}' is not a valid key for Vacancy")

    def __str__(self) -> str:
        """
        Return a string representation of the Vacancy object.
        """
        return (f"title: {self.title}\nvacancy URL: {self.vacancy_url}\n"
                f"salary from: {self.salary_from}\nsalary to: {self.salary_to}\n"
                f"employer: {self.employer}\ncity: {self.city}\nrequirements: {self.requirements}\n")

    def __lt__(self, other) -> bool:
        """
        Compares two Vacancy objects based on their average salary.

        Args:
            other (Vacancy): The other Vacancy object to compare.
        Returns:
            bool: True if this vacancy has a lower average salary than the other, False otherwise.
        """
        return self.salary_comparison < other.salary_comparison

    def __le__(self, other) -> bool:
        """
        Compares two Vacancy objects based on their average salary.

        Args:
            other (Vacancy): The other Vacancy object to compare.
        Returns:
            bool: True if this vacancy has a lower or equal average salary to the other, False otherwise.
        """
        return self.salary_comparison <= other.salary_comparison

    def __gt__(self, other) -> bool:
        """
        Compares two Vacancy objects based on their average salary.

        Args:
            other (Vacancy): The other Vacancy object to compare.
        Returns:
            bool: True if this vacancy has a higher average salary than the other, False otherwise.
        """
        return self.salary_comparison > other.salary_comparison

    def __ge__(self, other) -> bool:
        """
        Compares two Vacancy objects based on their average salary.

        Args:
            other (Vacancy): The other Vacancy object to compare.
        Returns:
            bool: True if this vacancy has a higher or equal average salary to the other, False otherwise.
        """
        return self.salary_comparison >= other.salary_comparison

    def __eq__(self, other) -> bool:
        """
        Compares two Vacancy objects based on their average salary.

        Args:
            other (Vacancy): The other Vacancy object to compare.
        Returns:
            bool: True if this vacancy has the same average salary as the other, False otherwise.
        """
        return self.salary_comparison == other.salary_comparison

    def to_dict(self) -> dict:
        """
        Converters the Vacancy object to a dictionary.

        Returns:
            dict: A dictionary containing the vacancy attributes.
        """
        vacancy_data = {
            'title': self.title,
            'vacancy_url': self.vacancy_url,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'employer': self.employer,
            'city': self.city,
            'requirements': self.requirements
        }

        return vacancy_data
