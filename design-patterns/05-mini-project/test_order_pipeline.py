import unittest

from order_pipeline import (
    AuditLoggingDecorator,
    BaseOrderProcessor,
    OrderBuilder,
    Receipt,
    StandardPricing,
    VipDiscountPricing,
)


class TestOrderPipeline(unittest.TestCase):
    def test_standard_order_pipeline_with_decorator_and_observer(self) -> None:
        order = (
            OrderBuilder("ORD-1", "Alice")
            .add_item("Book", 25.0, qty=2)
            .add_item("Pen", 5.0)
            .build()
        )
        audit_log: list[str] = []
        notified: list[Receipt] = []

        base = BaseOrderProcessor(StandardPricing())
        base.subscribe(notified.append)
        pipeline = AuditLoggingDecorator(base, audit_log)

        receipt = pipeline.process(order)

        self.assertEqual(receipt.total, 55.0)
        self.assertEqual(notified, [receipt])
        self.assertEqual(
            audit_log,
            ["START ORD-1 (Alice)", "DONE  ORD-1 total=$55.00"],
        )

    def test_vip_discount_strategy(self) -> None:
        order = OrderBuilder("ORD-2", "Bob").add_item("Monitor", 200.0).build()
        processor = BaseOrderProcessor(VipDiscountPricing(percent_off=25.0))
        receipt = processor.process(order)
        self.assertEqual(receipt.total, 150.0)


if __name__ == "__main__":
    unittest.main()
