import psycopg2
from psycopg2 import sql


def create_db(database, params):
    """
    Создание новой базы данных и таблиц в ней.
    """
    # Подключение к стандартной базе данных "postgres" для создания новой БД
    conn = psycopg2.connect(dbname="postgres", **params)
    # Установка кодировки клиента в UTF-8
    conn.set_client_encoding("UTF8")
    # Включение автоматического подтверждения транзакций
    conn.autocommit = True
    # Создание курсора для выполнения SQL-запросов
    cur = conn.cursor()

    # Удаление существующей базы данных с таким же именем, если она уже существует
    cur.execute(sql.SQL("DROP DATABASE IF EXISTS {};").format(sql.Identifier(database)))
    # Создание новой базы данных
    cur.execute(sql.SQL("CREATE DATABASE {};").format(sql.Identifier(database)))

    # Закрытие курсора и соединения
    cur.close()
    conn.close()

    # Подключение к созданной базе данных
    with psycopg2.connect(dbname=database, **params) as conn:
        # Создание курсора для выполнения SQL-запросов
        with conn.cursor() as cur:
            # Создание таблицы работодателей
            cur.execute(
                """CREATE TABLE employers (
                    company_id INTEGER PRIMARY KEY,
                    company_name TEXT NOT NULL);"""
            )

            # Создание таблицы вакансий
            cur.execute(
                """CREATE TABLE vacancies (
                        vacancy_id INTEGER PRIMARY KEY,
                        vacancy_name VARCHAR,
                        salary NUMERIC,
                        company_id INTEGER REFERENCES employers(company_id),
                        url VARCHAR);"""
            )
            # Фиксация изменений в базе данных
            conn.commit()
    # Завершение функции без возвращения значений
    return None


def save_to_db(database, vacancy, params):
    """
    Сохранение информации о вакансиях и работодателях в базу данных.
    """
    # Подключение к базе данных
    with psycopg2.connect(dbname=database, **params) as conn:
        # Включение автоматического подтверждения транзакций
        conn.autocommit = True
        # Создание курсора для выполнения SQL-запросов
        with conn.cursor() as cur:
            # Вставка записи о работодателе, игнорирование дубликатов по company_id
            cur.execute(
                """
                INSERT INTO employers (company_id, company_name) VALUES (%s, %s)
                ON CONFLICT (company_id) DO NOTHING;
            """,
                (vacancy.employer_id, vacancy.employer_name),
            )

            # Вставка записи о вакансии
            cur.execute(
                """
                INSERT INTO vacancies (vacancy_id, vacancy_name, salary, company_id, url) VALUES (%s, %s, %s, %s, %s);
            """,
                (vacancy.id, vacancy.name, vacancy.salary, vacancy.employer_id, vacancy.url),
            )
