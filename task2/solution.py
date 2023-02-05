def accum(string: str) -> str:
    '''
    Принимает на вход строку символов и преобразует ее в следующий вид:\n
    accum(“abcd”) -> “A-Bb-Ccc-Dddd”
    '''
    return '-'.join(
        [(letter * (index + 1)).capitalize() \
            for index, letter in enumerate(string)]
    )


if __name__ == '__main__':
    # Проверка:
    print(accum('abcd'))
