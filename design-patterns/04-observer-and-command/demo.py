from abc import ABC, abstractmethod
from typing import Callable


# --- Observer Pattern ---

class OrderEventBus:
    def __init__(self) -> None:
        self._listeners: list[Callable[[str], None]] = []

    def subscribe(self, listener: Callable[[str], None]) -> None:
        self._listeners.append(listener)

    def publish(self, order_id: str) -> None:
        for listener in self._listeners:
            listener(order_id)


# --- Command Pattern (with Undo) ---

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class TextBuffer:
    def __init__(self) -> None:
        self.text = ""


class AppendCommand(Command):
    def __init__(self, buf: TextBuffer, chunk: str) -> None:
        self._buf = buf
        self._chunk = chunk

    def execute(self) -> None:
        self._buf.text += self._chunk

    def undo(self) -> None:
        self._buf.text = self._buf.text[: -len(self._chunk)]


if __name__ == "__main__":
    # Observer demo
    bus = OrderEventBus()
    bus.subscribe(lambda oid: print(f"[Email] Sent receipt for {oid}"))
    bus.subscribe(lambda oid: print(f"[Analytics] Recorded sale {oid}"))
    bus.publish("ORD-1001")

    # Command + Undo demo
    buf = TextBuffer()
    history: list[Command] = []
    for chunk in ["Hello", ", ", "Patterns!"]:
        cmd = AppendCommand(buf, chunk)
        cmd.execute()
        history.append(cmd)

    print("After typing:", buf.text)
    history.pop().undo()
    print("After undo:  ", buf.text)
