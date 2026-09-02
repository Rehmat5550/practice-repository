class Calculator:
    def add(self, a : int, b : int) -> int:
        return a + b
    def division(self, a : int, b: int ) -> float:
        return a / b

calc = Calculator()
print(calc.add(4, 45))
print(calc.division(4, 23))