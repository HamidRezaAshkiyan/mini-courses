# Module 02: Ownership & Borrowing

Ownership is Rust's superpower: memory safety **without** a garbage collector.

## The Three Rules of Ownership

1. Every value in Rust has a single **owner**.
2. There can only be **one owner at a time** (assigning a `String` *moves* it; primitive `Copy` types like `i32` are copied).
3. When the owner goes out of scope, the value is **dropped** (freed) automatically.

## Borrowing Rules (References)

Instead of transferring ownership, you can *borrow* a value:
- **Any number of immutable references (`&T`)**, OR
- **Exactly one mutable reference (`&mut T`)** at a time.
- References must always be valid (no dangling pointers).

## Slices

- `&str` is a borrowed view into a UTF-8 string (works for both string literals and `&String`).
- `&[T]` is a borrowed view into a contiguous sequence (works for both arrays and `&Vec<T>`).

## Run the Lesson

From the `rust/` directory:

```bash
cargo run -p lesson-02-ownership
cargo test -p lesson-02-ownership
```

## Hands-On Exercises

Open [`src/main.rs`](./src/main.rs) and implement:
1. `first_word(s: &str) -> &str` — return a slice up to the first space (or the whole string if none).
2. `append_exclamation(s: &mut String)` — mutate the borrowed `String` in place.

Remove `#[ignore]` from their tests and run `cargo test -p lesson-02-ownership`.

---

Next: [Module 03 — Structs, Enums & Matching](../03-structs-enums-matching/README.md)
