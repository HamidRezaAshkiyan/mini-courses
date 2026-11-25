# Module 03: Adapter & Decorator

## 1. Adapter Pattern (Structural)

**Problem:** You want to integrate a third-party or legacy class whose method names or data format don't match the interface your application expects — and you can't (or shouldn't) modify that class.

**Solution:** Wrap the incompatible class in a small **Adapter** that implements your expected interface and translates calls to the underlying object.

## 2. Decorator Pattern (Structural)

**Problem:** You want to add cross-cutting behaviors (logging, caching, retries, compression, metrics) to an object dynamically without creating an explosion of subclasses (`CachedLoggedRetryingService`).

**Solution:** Wrap an object inside another object implementing the **same interface**, forwarding calls while adding behavior before/after.

**Real-world examples:** .NET `Stream` wrappers (`GZipStream`, `BufferedStream`), HTTP middleware pipelines.

## Run the Demo & Exercise

From `design-patterns/`:

```bash
python3 03-adapter-and-decorator/demo.py
python3 -m unittest 03-adapter-and-decorator/exercise.py
```

## Hands-On Task

Open [`exercise.py`](./exercise.py), remove `@unittest.skip(...)`, and implement:
1. `LegacyLoggerAdapter` — adapts `LegacyFileLogger.write_line(msg)` to the `Logger.log(level, msg)` interface.
2. `PrefixDecorator` — wraps any `Logger` and prepends a tag like `"[API] "` to every message.

---

Next: [Module 04 — Observer & Command](../04-observer-and-command/README.md)
