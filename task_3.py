def compress_string(strk):
    if not isinstance(strk, str):
        raise TypeError('strk must be a string')

    if not strk:
        return ""

    new_word, counter = '', 0
    for i in range(1, len(strk)):
        if strk[i] == strk[i-1]:
            counter += 1
        else:
            counter += 1
            new_word += f'{strk[i-1]}{counter}'
            counter = 0

    counter += 1
    new_word += f'{strk[-1]}{counter}'

    return new_word


if __name__ == '__main__':
    test_str = "aaabbbcccaaa"
    result = compress_string(test_str)
    print("Сжатая строка:", result)
