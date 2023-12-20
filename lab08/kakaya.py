def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred:{e}")
    return wrapper



@error_handler
def inner_func(min, max):
    def A(value):
        if min <= value <= max:
            print("Arguments are out of range")
        else:
            print("Arguments are with in renge")
    
    return A
A = inner_func(0,20)
A(30)
A('qwert')

