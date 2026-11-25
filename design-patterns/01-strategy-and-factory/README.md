# Module 01: Strategy & Factory

## 1. Strategy Pattern (Behavioral)

**Problem:** You have a giant `if / elif / else` block choosing between multiple algorithms (pricing rules, sorting, shipping rates, compression), and adding a new one forces you to edit the same method every time.

**Solution:** Define a common interface (strategy) for the algorithm, put each variant in its own class, and inject the chosen strategy into the context.

**Real-world examples:** .NET `IComparer<T>`, payment gateways, retry/backoff policies.

## 2. Factory Method / Simple Factory (Creational)

**Problem:** Calling code is tightly coupled to concrete classes (`if kind == "stripe": StripeGateway() ...`) scattered across your app.

**Solution:** Centralize creation behind a factory function/method that returns the abstract interface.

## Run the Demo & Exercise

From `design-patterns/`:

```bash
python3 01-strategy-and-factory/demo.py
python3 -m unittest 01-strategy-and-factory/exercise.py
```

## Hands-On Task

Open [`exercise.py`](./exercise.py), remove `@unittest.skip(...)`, and implement:
1. `ExpressShipping` and `FreeOver50Shipping` strategies.
2. `create_shipping_strategy(method: str)` factory function.

---

Next: [Module 02 — Builder & Singleton](../02-builder-and-singleton/README.md)
