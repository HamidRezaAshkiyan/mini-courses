from abc import ABC, abstractmethod


# --- Strategy Pattern ---

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, subtotal: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def apply(self, subtotal: float) -> float:
        return subtotal


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float) -> None:
        self.percent = percent

    def apply(self, subtotal: float) -> float:
        return round(subtotal * (1 - self.percent / 100.0), 2)


class FlatDiscount(DiscountStrategy):
    def __init__(self, amount: float) -> None:
        self.amount = amount

    def apply(self, subtotal: float) -> float:
        return max(0.0, round(subtotal - self.amount, 2))


# --- Factory ---

def create_discount(code: str) -> DiscountStrategy:
    factories: dict[str, DiscountStrategy] = {
        "NONE": NoDiscount(),
        "SAVE10": PercentageDiscount(10),
        "SAVE25": PercentageDiscount(25),
        "MINUS15": FlatDiscount(15),
    }
    if code not in factories:
        raise ValueError(f"Unknown promo code: {code}")
    return factories[code]


def checkout(subtotal: float, strategy: DiscountStrategy) -> float:
    return strategy.apply(subtotal)


if __name__ == "__main__":
    for code in ["NONE", "SAVE10", "MINUS15"]:
        strategy = create_discount(code)
        total = checkout(100.0, strategy)
        print(f"Promo {code:<7} -> $100.00 becomes ${total:.2f}")
