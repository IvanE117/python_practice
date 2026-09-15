def to_rna(dna):
    if not {'A', 'C', 'G', 'T'}.issuperset(set(dna)):
        raise ValueError('Invalid character')

    if not dna:
        return ''

    dt = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    result = list()
    for char in dna.upper():
        result.append(dt[char])

    return ''.join(result)


if __name__ == '__main__':
    # Пример использования
    sequence = "ACGTGGTCTTAA"
    print("РНК:", to_rna(sequence))
