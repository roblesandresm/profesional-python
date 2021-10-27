def is_prime(number: int) -> bool:
    result = [n for n in range(1, number + 1) if number % n == 0]
    return len(result) <= 2

def run():
    print(is_prime("4"))

if __name__ == "__main__":
    run()