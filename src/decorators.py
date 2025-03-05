from functools import wraps


def log(filename=None):
    """Логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки."""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e)}. Inputs: {args},{kwargs}"
            if filename:
                with open(filename, "a+") as file:
                    file.write(log_message)
            else:
                print(log_message)
            if "ok" in log_message:
                return result

        return inner

    return wrapper


@log("log.txt")
def divide(a, b):
    return a / b


divide(5, 2)
