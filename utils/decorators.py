def logger(func):

    def wrapper(*args, **kwargs):
        print("Executing", func.__name__)
        return func(*args, **kwargs)

    return wrapper