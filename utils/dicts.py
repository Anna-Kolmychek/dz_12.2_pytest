# функции для работы со словарями

def get_val(collection: dict, key, default='git'):
    """
    Возвращает значение по ключу. Если ключа нет, возвращает defoult
    :param collection: словарь
    :param key: ключ для поиска
    :param default: дефолтное значение для возврата, если ключа в словаре нет
    :return: значение в словаре по ключу
    """

    if key in collection.keys():
        return collection[key]

    return default
