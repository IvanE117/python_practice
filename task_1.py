def replace_characters(lst, old, new):
    if old == '' or lst == []:
        return lst

    for index, word in enumerate(lst[]):
        new_word = ''
        for i in range(len(word)):
            if word[i] == old:
                new_word += new
            else:
                new_word += word[i]
        lst[index] = new_word
    return lst


if __name__ == '__main__':
    test_list = ["hello", "world"]
    old_char = "o"
    new_char = "1"

    result = replace_characters(test_list, old_char, new_char)
    print("Результат:", result)