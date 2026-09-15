def replace_characters(lst, old, new):
    if old == '' or lst == []:
        return lst

    for index, word in enumerate(lst):
        new_word = ''
        for i in range(len(word)):
            if word[i] == old:
                new_word += new
            else:
                new_word += word[i]
        lst[index] = new_word
    return lst


if __name__ == '__main__':
    tests = [
        (["hello", "world"], "o", "1", ["hell1", "w1rld"]),
        (["apple", "banana", "cherry"], "a", "o", ["opple", "bonono", "cherry"]),
        (["abracadabra"], "a", "o", ["obrocodobro"]),
        ([], "a", "o", []),
        (["test"], "", "o", ["test"]),
        (["xyz"], "a", "o", ["xyz"]),
    ]

    for i, (lst, old, new, expected) in enumerate(tests, start=1):
        result = replace_characters(list(lst), old, new)  # копия, чтобы не портить данные теста
        status = "OK" if result == expected else "FAIL"
        print(f"Тест {i}: {status}")
        print(f"  Вход:     lst = {lst}, old = {old!r}, new = {new!r}")
        print(f"  Получено: {result}")
        print(f"  Ожидание: {expected}")
        print()
