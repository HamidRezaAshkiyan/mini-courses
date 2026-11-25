import unittest
from abc import ABC, abstractmethod
from typing import Any, Callable


class BankAccount:
    def __init__(self, balance: float = 0.0) -> None:
        self.balance = balance


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


# ============================================================================
# Hands-On Exercises
# ============================================================================

class DepositCommand(Command):
    """Exercise 1: Add `amount` to `account.balance` on execute(), subtract on undo()."""

    def __init__(self, account: BankAccount, amount: float) -> None:
        self._account = account
        self._amount = amount

    def execute(self) -> None:
        raise NotImplementedError("Implement DepositCommand.execute")

    def undo(self) -> None:
        raise NotImplementedError("Implement DepositCommand.undo")


class EventBus:
    """Exercise 2: Topic-based Observer bus supporting subscribe(topic, fn) and publish(topic, data)."""

    def __init__(self) -> None:
        self._subscribers: dict[str, list[Callable[[Any], None]]] = {}

    def subscribe(self, topic: str, handler: Callable[[Any], None]) -> None:
        raise NotImplementedError("Register handler under topic")

    def publish(self, topic: str, payload: Any) -> None:
        raise NotImplementedError("Invoke all handlers subscribed to topic with payload")


class TestObserverAndCommand(unittest.TestCase):
    def test_example_account(self) -> None:
        acc = BankAccount(100.0)
        self.assertEqual(acc.balance, 100.0)

    @unittest.skip("Hands-on exercise: remove @unittest.skip and implement DepositCommand")
    def test_deposit_command_and_undo(self) -> None:
        acc = BankAccount(50.0)
        cmd = DepositCommand(acc, 25.0)
        cmd.execute()
        self.assertEqual(acc.balance, 75.0)
        cmd.undo()
        self.assertEqual(acc.balance, 50.0)

    @unittest.skip("Hands-on exercise: remove @unittest.skip and implement EventBus")
    def test_event_bus(self) -> None:
        bus = EventBus()
        received: list[str] = []
        bus.subscribe("user.created", lambda name: received.append(f"welcome:{name}"))
        bus.subscribe("user.created", lambda name: received.append(f"audit:{name}"))
        bus.publish("user.created", "Alice")
        bus.publish("other.event", "ignored")
        self.assertEqual(received, ["welcome:Alice", "audit:Alice"])


if __name__ == "__main__":
    unittest.main()
