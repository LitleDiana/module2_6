calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    lenght = len(string)  # Длина строки
    upper_case = string.upper()  # Строка в верхнем регистре
    lower_case = string.lower()  # Строка в нижнем регистре
    return lenght, upper_case, lower_case  # Возвращаем кортеж


def is_contains(string, list_to_search):
    count_calls()
    # Приводим строку к нижнему регистру
    lower_string = string.lower()

    # Проверяем, содержится ли приведенная к нижнему регистру строка в списке (приведенном к нижнему регистру)
    return lower_string in (item.lower() for item in list_to_search)


result1 = string_info("Hello, World!")
result2 = is_contains("UrbaN", ["apple", "banana", "urban"])
result3 = string_info("Python Programming")
result4 = is_contains("example", ["test", "sample", "Example"])

# Вывод результатов
print(result1)  # Вывод: (13, 'HELLO, WORLD!', 'hello, world!')
print(result2)  # Вывод: True
print(result3)  # Вывод: (18, 'PYTHON PROGRAMMING', 'python programming')
print(result4)  # Вывод: True

# Вывод значения переменной calls
print("Количество вызовов функций:", calls)  # Вывод: Количество вызовов функций: 4
