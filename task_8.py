def rotate(mat):
    if (
        not isinstance(mat, list)
        or not all(isinstance(elem, list) for elem in mat)
    ):
        raise TypeError

    if not mat:
        return []

    if not all(len(row) == len(mat) for row in mat):
        raise ValueError

    rotated = []
    for i in range(len(mat)):
        row = [
            mat[j][i] for j in range(len(mat) - 1, -1, -1)
        ]
        rotated.append(row)
    return rotated


if __name__ == '__main__':
    # Пример использования
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(rotate(m))
