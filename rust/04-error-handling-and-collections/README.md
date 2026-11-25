# Module 04: Error Handling & Collections

## Core Concepts

1. **No exceptions:** Rust represents recoverable errors with `Result<T, E>` (`Ok(value)` or `Err(error)`).
2. **The `?` operator:** Propagates an `Err` early from a function returning `Result`, keeping the happy path clean.
3. **Standard collections:**
   - `Vec<T>` — growable array on the heap.
   - `HashMap<K, V>` — hash table with an ergonomic `.entry(key).or_insert(default)` API.
   - Iterators (`.iter()`, `.map()`, `.filter()`, `.collect()`) — zero-cost abstractions over collections.

## Run the Lesson

From the `rust/` directory:

```bash
cargo run -p lesson-04-errors
cargo test -p lesson-04-errors
```

## Hands-On Exercises

Open [`src/main.rs`](./src/main.rs) and implement:
1. `parse_and_sum(lines: &[&str]) -> Result<i32, std::num::ParseIntError>` using the `?` operator.
2. `word_counts(text: &str) -> HashMap<String, usize>` counting lowercase words in a string.

Remove `#[ignore]` from their tests and run `cargo test -p lesson-04-errors`.

---

Next: [Module 05 — Mini Project: CLI Task Tracker](../05-mini-project/README.md)
