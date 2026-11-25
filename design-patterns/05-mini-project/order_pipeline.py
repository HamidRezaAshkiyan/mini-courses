from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable


# --- 1. Builder ---

@dataclass(frozen=True)
class OrderItem:
    name: str
    price: float
    qty: int = 1


@dataclass(frozen=True)
class Order:
    order_id: str
    customer: str
    items: tuple[OrderItem, ...]


class OrderBuilder:
    def __init__(self, order_id: str, customer: str) -> None:
        self._order_id = order_id
        self._customer = customer
        self._items: list[OrderItem] = []

    def add_item(self, name: str, price: float, qty: int = 1) -> "OrderBuilder":
        if price < 0 or qty <= 0:
            raise ValueError("Invalid item price or quantity")
        self._items.append(OrderItem(name=name, price=price, qty=qty))
        return self

    def build(self) -> Order:
        return Order(
            order_id=self._order_id,
            customer=self._customer,
            items=tuple(self._items),
        )


# --- 2. Strategy ---

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_total(self, order: Order) -> float:
        pass


class StandardPricing(PricingStrategy):
    def calculate_total(self, order: Order) -> float:
        return round(sum(i.price * i.qty for i in order.items), 2)


class VipDiscountPricing(PricingStrategy):
    def __init__(self, percent_off: float = 20.0) -> None:
        self._percent_off = percent_off

    def calculate_total(self, order: Order) -> float:
        subtotal = sum(i.price * i.qty for i in order.items)
        return round(subtotal * (1.0 - self._percent_off / 100.0), 2)


# --- 3. Processor + Decorator + 4. Observer ---

@dataclass(frozen=True)
class Receipt:
    order_id: str
    customer: str
    total: float


class OrderProcessor(ABC):
    @abstractmethod
    def process(self, order: Order) -> Receipt:
        pass


class BaseOrderProcessor(OrderProcessor):
    def __init__(self, pricing: PricingStrategy) -> None:
        self._pricing = pricing
        self._observers: list[Callable[[Receipt], None]] = []

    def subscribe(self, observer: Callable[[Receipt], None]) -> None:
        self._observers.append(observer)

    def process(self, order: Order) -> Receipt:
        total = self._pricing.calculate_total(order)
        receipt = Receipt(order_id=order.order_id, customer=order.customer, total=total)
        for observer in self._observers:
            observer(receipt)
        return receipt


class AuditLoggingDecorator(OrderProcessor):
    def __init__(self, inner: OrderProcessor, log_sink: list[str]) -> None:
        self._inner = inner
        self._log_sink = log_sink

    def process(self, order: Order) -> Receipt:
        self._log_sink.append(f"START {order.order_id} ({order.customer})")
        receipt = self._inner.process(order)
        self._log_sink.append(f"DONE  {receipt.order_id} total=${receipt.total:.2f}")
        return receipt


if __name__ == "__main__":
    order = (
        OrderBuilder("ORD-42", "Hamid")
        .add_item("Mechanical Keyboard", 120.0)
        .add_item("USB-C Cable", 15.0, qty=2)
        .build()
    )

    audit_log: list[str] = []
    base = BaseOrderProcessor(VipDiscountPricing(percent_off=10.0))
    base.subscribe(lambda r: print(f"[Email] Receipt sent to {r.customer}: ${r.total:.2f}"))

    pipeline: OrderProcessor = AuditLoggingDecorator(base, audit_log)
    receipt = pipeline.process(order)

    print("Receipt:", receipt)
    print("Audit log:", audit_log)
