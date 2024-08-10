def get_multiplied_digits(number):
    # Преобразование числа в строковое представление
    str_number = str(number)
    
    # Если длина str_number равна 1, верните само число.
    if len(str_number) <= 1:
        return int(str_number)
    
    # Получить первую цифру как целое число
    first = int(str_number[0])
    
    # Recursively call the function with the rest of the number (excluding the first digit
    return first * get_multiplied_digits(int(str_number[1:]))

# Пример использования
result = get_multiplied_digits(40203)
print(result)  # Результат должен быть 24