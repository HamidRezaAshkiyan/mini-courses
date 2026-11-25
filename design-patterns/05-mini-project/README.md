# Module 05: Mini Project — Order Processing Pipeline

See how **four patterns work together cleanly** in a tiny, realistic e-commerce checkout pipeline:

| Pattern | Role in the Pipeline |
| --- | --- |
| **Builder** | `OrderBuilder` constructs a validated, immutable `Order` |
| **Strategy** | `PricingStrategy` swaps pricing rules (standard vs VIP discount) |
| **Decorator** | `LoggingProcessor` wraps `OrderProcessor` to record audit logs without modifying core logic |
| **Observer** | Subscribers receive `OrderCompleted` notifications automatically |

## Run & Test

From `design-patterns/`:

```bash
python3 05-mini-project/order_pipeline.py
python3 -m unittest discover -s 05-mini-project
```

## Stretch Challenges (Hands-On Practice)

1. **Add a `BuyOneGetOneStrategy`** (or `BulkDiscountStrategy` giving 15% off when total quantity ≥ 5) without modifying `BaseOrderProcessor`.
2. **Add a `ValidationDecorator`** wrapping `OrderProcessor` that rejects orders with an empty item list before delegating.
3. **Add a second Observer** (e.g., `LoyaltyPointsObserver` that awards 1 point per \$10 spent) and test it in [`test_order_pipeline.py`](./test_order_pipeline.py).

---

Congratulations! You've practiced the core creational, structural, and behavioral patterns that show up in almost every production backend and frontend architecture.
