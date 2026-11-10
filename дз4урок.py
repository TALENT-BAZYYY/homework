rates = {
    "KGS": 1,
    "USD": 89,
    "EUR": 96,
    "RUB": 1.2
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency.upper()

    def convert_to_kgs(self):
        return self.amount * rates[self.currency]

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if isinstance(other, Money):
            total_in_kgs = self.convert_to_kgs() + other.convert_to_kgs()
            return Money(total_in_kgs, "KGS")
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Money):
            total_in_kgs = self.convert_to_kgs() - other.convert_to_kgs()
            return Money(total_in_kgs, "KGS")
        return NotImplemented

    def __mul__(self, number):
        if isinstance(number, (int, float)):
            return Money(self.amount * number, self.currency)
        return NotImplemented

    def __truediv__(self, number):
        if isinstance(number, (int, float)):
            if number == 0:
                raise ZeroDivisionError()
            return Money(self.amount / number, self.currency)
        return NotImplemented


if __name__ == "__main__":
    money1 = Money(100, "USD")
    money2 = Money(5000, "KGS")

    result = money1 + money2
    print(result)
