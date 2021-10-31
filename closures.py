def make_repeater_of(n: int):
    def repeater(word: str) -> str:
        assert type(word) == str, "Solo puedes usar cadenas"
        return word * n
    return repeater

def make_division_by(n: int):
    def numerator(x: int) -> int:
        assert n != 0 and n > 0, "No se puede dividir por cero o entero negativo"
        return int(x / n)
    return numerator

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hi"))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("Hello"))
    division_by_6 = make_division_by(6)
    print(division_by_6(36))

if __name__ == "__main__":
    run()