import traceback
from colorama import Fore, Style

def divider(a, b):
    try:
        if a < b:
            raise ValueError("Делимое должно быть больше или равно делителю")
        if b > 100:
            raise IndexError("Делитель не должен превышать 100")
        return a / b
    except (TypeError, ZeroDivisionError, ValueError, IndexError) as e:
        print(Fore.RED + f"Ошибка: {type(e).__name__}: {str(e)}" + Style.RESET_ALL)
        traceback.print_exc()

def process_data(data):
    result = []
    for key, value in data.items():
        try:
            res = divider(key, value)
            result.append(res)
        except (KeyError, TypeError) as e:
            print(Fore.YELLOW + f"Ошибка с ключом {key}: {type(e).__name__}" + Style.RESET_ALL)
            traceback.print_exc()  # Добавим вывод полной трассировки ошибки
    return result

if __name__ == "__main__":
    # Заменим список [] на строку, так как списки не могут быть ключами в словарях
    data = {10: 2, 2: 5, "123": 4, 18: 0, "list_key": 15, 8: 4}
    results = process_data(data)
    print(Fore.GREEN + f"Результаты: {results}" + Style.RESET_ALL)
