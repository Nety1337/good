#1
def message_decorator(func):
    def wrapper():
        print("Начало выполнения функции")
        func()
        print("Конец выполнения функции")
    return wrapper

@message_decorator
def my_function():
    print("Выполнение функции")

my_function()

print()

#2
def message_decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(f"Начало выполнения функции с аргументами {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Конец выполнения функции. Результат: {result}")
        return result
    return wrapper

@message_decorator_with_args
def sum_numbers(a, b):
    return a + b

print(sum_numbers(2, 3))