def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred:{e}")
    return wrapper



@error_handler
def check_range(min_value, max_value):
    def closure(value):
        try:
            num_value = float(value)  # Преобразуем введенное значение в число
            return min_value <= num_value <= max_value
        except ValueError:
            return False  # Если произошла ошибка при преобразовании в число, возвращаем False
    return closure

# Пример использования
check_age = check_range(18, 100)
print(check_age(25))  # True
print(check_age('abc'))  # False


