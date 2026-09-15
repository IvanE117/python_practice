def count_char(lst, char):
    if not isinstance(char, str) or len(char) != 1:
        raise ValueError("char must contain exactly one character")

    if not isinstance(lst, list) or not all(isinstance(elem, str) for elem in lst):
        raise TypeError("lst must be a list of strings")

    counter_list = []
    for word in lst:
        counter = 0
        for ch in word:
            if ch == char:
                counter += 1
        counter_list.append(counter)
    return counter_list


if __name__ == "__main__":
    test_list = ["helloo", "world"]
    char_to_count = "o"

    result = count_char(test_list, char_to_count)
    print("Результат:", result)