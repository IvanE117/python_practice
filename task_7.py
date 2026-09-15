def is_palindrome(strk):
    if not isinstance(strk, str):
        raise TypeError('strk must be str')
    return strk == strk[::-1]


if __name__ == '__main__':
    print(is_palindrome("racecar"))
    print(is_palindrome("racecar"))         # True
    print(is_palindrome("football"))        # False
    print(is_palindrome("madam"))           # True
    print(is_palindrome("12321"))           # True
    print(is_palindrome("Hello"))           # False
    print(is_palindrome(""))
