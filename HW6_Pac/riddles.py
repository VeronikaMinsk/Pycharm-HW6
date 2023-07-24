__all__ = ["secrets", "storage"]

def secrets(puzzle: str, answers: list[str], count=3) -> int:
    print(f'Угадай загадку.\n{puzzle}')
    for i in range(1, count+1):
        ans = input(f'Попытка номер {i}: ').lower()
        if ans in answers:
            return i
    return 0

def storage():
    puzzles = {
        'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
        'Не лает, не кусает, в дом не пускает': ['замок'],
        'Сидит дед во сто шуб одет': ['лук', 'луковица'],
    }
    for key, value in puzzles.items():
        result = secrets(key, value)
        print(f'Угадал с {result} попытки' if result > 0 else 'Не угадал')

