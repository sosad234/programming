def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred:{e}")
    return wrapper



@error_handler
def func(arg1, arg2):
    if (arg1 < 0  or arg1 > 100) or (arg2 < 0  or arg2 > 100):
        raise ValueError("Arguments are out of range")
    else:
        print("Arguments are with in renge")
func(50,75)
func(150,75)

