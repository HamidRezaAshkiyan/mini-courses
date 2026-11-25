# Module 03: Structs, Enums & Pattern Matching

## Core Concepts

1. **Structs** group named fields together, and `impl` blocks attach methods (`&self`, `&mut self`, or associated constructors like `Self::new(...)`).
2. **Enums in Rust are tagged unions (algebraic data types):** each variant can hold different data!
3. **No `null`!** Rust uses `Option<T>` (`Some(value)` or `None`) so the compiler forces you to handle missing values.
4. **`match` is exhaustive:** the compiler guarantees you didn't forget a variant.

## Run the Lesson

From the `rust/` directory:

```bash
cargo run -p lesson-03-types
cargo test -p lesson-03-types
```

## Hands-On Exercises

Open [`src/main.rs`](./src/main.rs) and implement:
1. `Shape::area(&self) -> f64` using `match` on `Shape::Circle` and `Shape::Rectangle`.
2. `find_first_negative(nums: &[i32]) -> Option<i32>` returning `Some(n)` or `None`.

Remove `#[ignore]` from their tests and run `cargo test -p lesson-03-types`.

---

Next: [Module 04 — Error Handling & Collections](../04-error-handling-and-collections/README.md)
