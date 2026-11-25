# Module 01: Rust Basics

## Core Concepts

1. **Immutable by default:** `let x = 5;` cannot be reassigned unless you opt in with `let mut x = 5;`.
2. **Shadowing:** You can re-declare `let x = x + 1;` (even changing its type).
3. **Expression-oriented:** Blocks, `if`, and `match` evaluate to values. The last expression without a semicolon (`;`) is the return value.
4. **Strict types:** No implicit numeric coercion (`i32` won't silently become `f64`).

## Run the Lesson

From the `rust/` directory:

```bash
cargo run -p lesson-01-basics
cargo test -p lesson-01-basics
```

## Hands-On Exercises

Open [`src/main.rs`](./src/main.rs), scroll to the bottom, and implement:
1. `celsius_to_fahrenheit(c: f64) -> f64`
2. `sum_even_up_to(n: u32) -> u32`

Remove `#[ignore]` from their tests and run `cargo test -p lesson-01-basics` until all tests pass.

---

Next: [Module 02 — Ownership & Borrowing](../02-ownership-and-borrowing/README.md)
