import psycopg2


class DBManager:
    """Класс для управления соединением с базой данных PostgreSQL."""

    def __init__(self, database, params):
        """
        Инициализация подключения к базе данных.
        """
        self.database = database
        self.params = params
        # Устанавливаем соединение с базой данных
        self.conn = psycopg2.connect(dbname=self.database, **self.params)
        # Создаём курсор для выполнения SQL-запросов
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """
        Получение списка компаний и количества вакансий для каждой компании.
        """
        # Запрашиваем данные о компаниях и количестве вакансий
        self.cur.execute("SELECT company_name, COUNT(*) FROM vacancies GROUP BY company_name")
        # Возвращаем результат выборки
        return self.cur.fetchall()

    def get_all_vacancies(self):
        """
        Получение всех вакансий из базы данных.
        """
        # Выполняем запрос на получение всех вакансий
        self.cur.execute("SELECT * FROM vacancies")
        # Возвращаем результат выборки
        return self.cur.fetchall()

    def get_avg_salary(self):
        """
        Получение среднего значения зарплаты по всем вакансиям.
        """
        # Выполняем запрос на вычисление среднего значения зарплаты
        self.cur.execute("SELECT AVG(salary) FROM vacancies")
        # Преобразуем результат выборки в число с плавающей точкой
        return float(self.cur.fetchall()[0][0])

    def get_vacancies_with_higher_salary(self):
        """
        Получение списка вакансий с зарплатой выше средней.
        """
        # Получаем среднее значение зарплаты
        avg_salary = self.get_avg_salary()
        # Выполняем запрос на получение вакансий с зарплатой выше средней
        self.cur.execute("SELECT * FROM vacancies WHERE salary > %s", (avg_salary,))
        # Возвращаем результат выборки
        return self.cur.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        """
        Получение списка вакансий, содержащих указанный ключевой слово.
        """
        # Выполняем запрос на поиск вакансий по ключевому слову
        self.cur.execute(f"SELECT * FROM vacancies WHERE description ILIKE '%{keyword}%'")
        # Возвращаем результат выборки
        return self.cur.fetchall()
