import time

def fibo_gen(max):
    n1, n2  = 0, 1
    while n1 <= max:
        yield n1
        n1, n2 = n2, n1+n2

if __name__ == "__main__":
    fibonacci = fibo_gen(700)
    for element in fibonacci:
        print(element)
        time.sleep(1)
