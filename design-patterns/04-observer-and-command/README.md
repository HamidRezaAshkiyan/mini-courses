# Module 04: Observer & Command

## 1. Observer Pattern (Behavioral)

**Problem:** When an important event happens (e.g., an order is placed), you don't want the `OrderService` to directly know about `EmailService`, `InventoryService`, `AnalyticsService`, and `SlackNotifier`.

**Solution:** Maintain a list of **subscribers (observers)**. When an event occurs, notify all subscribers — adding or removing listeners requires zero changes to the publisher.

**Real-world examples:** C# `event` / `IObservable<T>`, DOM `addEventListener`, message brokers / webhooks.

## 2. Command Pattern (Behavioral)

**Problem:** You want to queue operations, log them, or support **Undo / Redo** without hardcoding reversal logic into UI buttons or controllers.

**Solution:** Encapsulate each action as an object with `execute()` and `undo()` methods, and push executed commands onto a history stack.

## Run the Demo & Exercise

From `design-patterns/`:

```bash
python3 04-observer-and-command/demo.py
python3 -m unittest 04-observer-and-command/exercise.py
```

## Hands-On Task

Open [`exercise.py`](./exercise.py), remove `@unittest.skip(...)`, and implement:
1. `BankAccount` + `DepositCommand` with working `execute()` and `undo()`.
2. `EventBus` supporting `subscribe(event_name, handler)` and `publish(event_name, payload)`.

---

Next: [Module 05 — Mini Project: Order Processing Pipeline](../05-mini-project/README.md)
