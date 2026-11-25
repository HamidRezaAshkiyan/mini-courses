import unittest
from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, level: str, message: str) -> None:
        pass


class LegacyLineWriter:
    """Incompatible legacy class we cannot modify."""

    def __init__(self) -> None:
        self.lines: list[str] = []

    def write_line(self, text: str) -> None:
        self.lines.append(text)


# ============================================================================
# Hands-On Exercises
# ============================================================================

class LegacyLoggerAdapter(Logger):
    """Exercise 1: Adapt LegacyLineWriter so `log("INFO", "started")`
    calls `writer.write_line("[INFO] started")`.
    """

    def __init__(self, writer: LegacyLineWriter) -> None:
        self._writer = writer

    def log(self, level: str, message: str) -> None:
        raise NotImplementedError("Format '[LEVEL] message' and call self._writer.write_line")


class PrefixLoggerDecorator(Logger):
    """Exercise 2: Wrap any Logger and prepend `f'{prefix}: '` to `message`."""

    def __init__(self, inner: Logger, prefix: str) -> None:
        self._inner = inner
        self._prefix = prefix

    def log(self, level: str, message: str) -> None:
        raise NotImplementedError("Forward to self._inner.log with prefixed message")


class TestAdapterAndDecorator(unittest.TestCase):
    def test_example_legacy_writer(self) -> None:
        writer = LegacyLineWriter()
        writer.write_line("hello")
        self.assertEqual(writer.lines, ["hello"])

    @unittest.skip("Hands-on exercise: remove @unittest.skip and implement LegacyLoggerAdapter")
    def test_adapter(self) -> None:
        writer = LegacyLineWriter()
        logger = LegacyLoggerAdapter(writer)
        logger.log("INFO", "server started")
        self.assertEqual(writer.lines, ["[INFO] server started"])

    @unittest.skip("Hands-on exercise: remove @unittest.skip and implement PrefixLoggerDecorator")
    def test_decorator(self) -> None:
        writer = LegacyLineWriter()
        logger: Logger = PrefixLoggerDecorator(LegacyLoggerAdapter(writer), "AUTH")
        logger.log("WARN", "invalid token")
        self.assertEqual(writer.lines, ["[WARN] AUTH: invalid token"])


if __name__ == "__main__":
    unittest.main()
