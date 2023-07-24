from random import randint

__all__ = ["guess"]

def guess(lower: int = 0, upper: int = 100, count: int = 10) -> bool:
    number = randint(lower, upper)
    for _ in range(count):
        answer = int(input(f'Введите число между [{lower}, {upper}]: '))
        if answer < number:
            print(f'Число {answer} меньше загаданного')
        elif answer > number:
            print(f'Число {answer} больше загаданного')
        else:
            return True
    return False
