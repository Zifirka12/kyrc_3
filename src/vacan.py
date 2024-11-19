class Vacancy:
    """
    Класс для представления вакансии.
    """

    def __init__(self, vacancy):
        """
        Конструктор класса. Инициализирует атрибуты объекта на основе переданного словаря с данными вакансии.
        """
        self.name = vacancy["name"]  # Назначение названия вакансии
        if vacancy["salary"]:  # Проверка наличия зарплаты
            self.salary = vacancy["salary"]["from"]  # Присвоение минимальной зарплаты
        else:
            self.salary = None  # Если зарплата отсутствует, присваивается None
        self.url = vacancy["url"]  # Назначение ссылки на вакансию
        self.id = vacancy["id"]  # Назначение идентификатора вакансии
        self.employer_name = vacancy["employer"]["name"]  # Назначение имени работодателя
        self.employer_id = vacancy["employer"]["id"]  # Назначение идентификатора работодателя

    def __lt__(self, other):
        """
        Метод для сравнения двух объектов Vacancy по зарплате.
        """
        if isinstance(other, Vacancy):  # Проверка типа сравниваемого объекта
            return self.salary < other.salary  # Сравнение зарплат
        else:
            print("Вы пытаетесь сравнить объекты разных классов")  # Сообщение об ошибке, если типы объектов разные

    def __gt__(self, other):
        """
        Метод для сравнения двух объектов Vacancy по зарплате.
        """
        if isinstance(other, Vacancy):  # Проверка типа сравниваемого объекта
            return self.salary > other.salary  # Сравнение зарплат
        else:
            print("Вы пытаетесь сравнить объекты разных классов")  # Сообщение об ошибке, если типы объектов разные

    def __repr__(self):
        """
        Метод для строкового представления объекта Vacancy.
        """
        return f'{{{"name": "{self.name}", "salary": {self.salary}, "url": "{self.url}"}}}'
