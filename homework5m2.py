from datetime import datetime
from functools import wraps


def checktime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S %d/%m/%Y")
        print(f"функция была вызвана в {time_str}")
        return func(*args, **kwargs)
    return wrapper


@checktime
def hello_world(name):
    print(f"hello world from {name}")