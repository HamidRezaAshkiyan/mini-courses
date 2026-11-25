# Design Patterns — Mini Course

Learn the **8 most practical software design patterns** you'll actually encounter in real codebases — through concise explanations, runnable Python 3 demos, and hands-on unit-tested exercises (zero external dependencies).

> The examples use clean, type-annotated Python (`ABC`, `@dataclass`) so they run anywhere with `python3` and translate directly to C#, Java, TypeScript, or Go.

## Prerequisites

- Python 3.10+ (`python3 --version`)
- Basic familiarity with classes and interfaces

## How This Course Works

For each module:
1. Read its `README.md` to understand **the problem** the pattern solves (and when *not* to use it).
2. Run the working demo:
   ```bash
   python3 01-strategy-and-factory/demo.py
   ```
3. Open `exercise.py`, remove `@unittest.skip(...)` from the exercise tests, and implement the `NotImplementedError` stubs until:
   ```bash
   python3 -m unittest 01-strategy-and-factory/exercise.py
   ```
   passes green!

## Syllabus

| # | Module | Category | Patterns Covered |
| --- | --- | --- | --- |
| 01 | [Strategy & Factory](./01-strategy-and-factory/README.md) | Behavioral + Creational | Swappable algorithms, decoupled object creation |
| 02 | [Builder & Singleton](./02-builder-and-singleton/README.md) | Creational | Fluent object construction, shared instances (and DI tradeoffs) |
| 03 | [Adapter & Decorator](./03-adapter-and-decorator/README.md) | Structural | Bridging incompatible APIs, layering behavior without subclassing |
| 04 | [Observer & Command](./04-observer-and-command/README.md) | Behavioral | Event pub/sub decoupling, actions with Undo/Redo |
| 05 | [Mini Project: Order Pipeline](./05-mini-project/README.md) | Combined | Builder + Strategy + Decorator + Observer working together |

## Golden Rule of Design Patterns

**Never force a pattern where simple code works.** Patterns are a shared vocabulary for solving recurring structural problems — reach for them when you feel real pain (growing `if/elif` chains, rigid constructors, duplicated cross-cutting logic, tight coupling).
