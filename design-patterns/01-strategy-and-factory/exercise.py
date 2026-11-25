import unittest
from abc import ABC, abstractmethod


class ShippingStrategy(ABC):
    @abstractmethod
    def cost(self, order_total: float, weight_kg: float) -> float:
        pass


class StandardShipping(ShippingStrategy):
    def cost(self, order_total: float, weight_kg: float) -> float:
        return round(5.0 + 1.5 * weight_kg, 2)


# ============================================================================
# Hands-On Exercises
# Remove @unittest.skip(...) below and implement these classes/functions.
# ============================================================================

class ExpressShipping(ShippingStrategy):
    """Exercise 1: Express costs $15.00 base + $3.00 per kg."""

    def cost(self, order_total: float, weight_kg: float) -> float:
        raise NotImplementedError("Implement ExpressShipping.cost")


class FreeOver50Shipping(ShippingStrategy):
    """Exercise 2: Free ($0.0) if order_total >= 50.0, else StandardShipping cost."""

    def cost(self, order_total: float, weight_kg: float) -> float:
        raise NotImplementedError("Implement FreeOver50Shipping.cost")


def create_shipping_strategy(method: str) -> ShippingStrategy:
    """Exercise 3: Return StandardShipping, ExpressShipping, or FreeOver50Shipping
    for 'standard', 'express', or 'free_over_50'. Raise ValueError otherwise.
    """
    raise NotImplementedError("Implement create_shipping_strategy factory")


class TestShippingExercise(unittest.TestCase):
    def test_example_standard_shipping(self) -> None:
        self.assertEqual(StandardShipping().cost(30.0, 2.0), 8.0)

    @unittest.skip("Hands-on exercise: remove @unittest.skip and implement ExpressShipping")
    def test_express_shipping(self) -> None:
        self.assertEqual(ExpressShipping().cost(30.0, 2.0), 21.0)

    @unittest.skip("Hands-on exercise: remove @unittest.skip and implement FreeOver50Shipping")
    def test_free_over_50_shipping(self) -> None:
        strategy = FreeOver50Shipping()
        self.assertEqual(strategy.cost(50.0, 4.0), 0.0)
        self.assertEqual(strategy.cost(49.99, 2.0), 8.0)

    @unittest.skip("Hands-on exercise: remove @unittest.skip and implement create_shipping_strategy")
    def test_factory(self) -> None:
        self.assertIsInstance(create_shipping_strategy("standard"), StandardShipping)
        self.assertIsInstance(create_shipping_strategy("express"), ExpressShipping)
        self.assertIsInstance(create_shipping_strategy("free_over_50"), FreeOver50Shipping)
        with self.assertRaises(ValueError):
            create_shipping_strategy("drone")


if __name__ == "__main__":
    unittest.main()
