from configparser import ConfigParser


def config(filename="database.ini", section="postgresql"):
    """
    Функция для чтения конфигурации из файла .ini и возврата параметров секции.
    """
    # Создаем объект парсера для работы с конфигурационными файлами
    parser = ConfigParser()
    # Читаем указанный файл конфигурации
    parser.read(filename)
    # Создаем пустой словарь для хранения параметров секции
    db = {}
    # Проверяем наличие указанной секции в файле конфигурации
    if parser.has_section(section):
        # Извлекаем параметры из секции и добавляем их в словарь
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        # Генерируем исключение, если секция не найдена
        raise Exception('Section {0} is not found in the {1} file.'.format(section, filename))
    # Возвращаем словарь с параметрами секции
    return db
