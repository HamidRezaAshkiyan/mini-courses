# Module 02: Builder & Singleton

## 1. Builder Pattern (Creational)

**Problem:** A constructor with 8 optional parameters (`HttpRequest("POST", url, None, None, 30, True, ...)`) is hard to read, easy to mix up, and painful to validate.

**Solution:** Construct the object step-by-step via a fluent builder (`return self`), finishing with `.build()` that validates and returns an immutable result.

**Real-world examples:** C# `StringBuilder` / `WebApplicationBuilder`, SQL query builders, HTTP request builders.

## 2. Singleton Pattern (Creational)

**Problem:** You want exactly one shared instance of a resource (e.g., app configuration, connection pool).

**Caution:** Singletons introduce global state and make unit testing harder. In modern apps (like ASP.NET Core or Spring), prefer **Dependency Injection** with a singleton lifetime over hand-rolled global singletons.

## Run the Demo & Exercise

From `design-patterns/`:

```bash
python3 02-builder-and-singleton/demo.py
python3 -m unittest 02-builder-and-singleton/exercise.py
```

## Hands-On Task

Open [`exercise.py`](./exercise.py), remove `@unittest.skip(...)`, and complete `SqlQueryBuilder` so it builds `SELECT ... FROM ... WHERE ... LIMIT ...` queries fluently.

---

Next: [Module 03 — Adapter & Decorator](../03-adapter-and-decorator/README.md)
