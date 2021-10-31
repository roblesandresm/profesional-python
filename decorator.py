from datetime import datetime

def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"Pasaron {time_elapsed.total_seconds()} segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(10000000):
        pass

@execution_time
def suma(a: int, b:int) -> int:
    print(a + b)

@mayusculas
def message(nombre):
    return f"{nombre}, Recobiste un mensaje"

# print(message("Andres"))
random_func()
suma(5, 10)