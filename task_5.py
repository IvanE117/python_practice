def filter_dict_by_value(d, threshold):
    return {key: value for key, value in d.items() if value > threshold}


if __name__ == '__main__':
    # Пример использования
    data = {'a': 1, 'b': 2, 'c': 3}
    limit = 2
    result = filter_dict_by_value({'x': 10, 'y': 5, 'z': 8}, 7)
    print("Результат:", result)
