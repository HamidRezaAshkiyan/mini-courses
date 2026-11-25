# Rust Basics — Mini Course

Learn the fundamentals of Rust through short explanations, runnable examples, and test-driven hands-on exercises — using **zero external dependencies**.

## Prerequisites

- Rust toolchain installed via [rustup](https://rustup.rs/):
  ```bash
  rustc --version
  cargo --version
  ```

## How This Course Works

The entire `rust/` folder is a **Cargo workspace**. From inside `rust/`, you can run or test any module:

```bash
# Run a lesson's interactive demo
cargo run -p lesson-01-basics

# Run the passing example tests
cargo test -p lesson-01-basics

# See the hands-on exercise tests (marked with #[ignore] until you implement them)
cargo test -p lesson-01-basics -- --ignored
```

For each module:
1. Read its `README.md`.
2. Run `cargo run -p <package>` and read `src/main.rs`.
3. Open `src/main.rs`, remove `#[ignore]` from the exercise tests at the bottom, and implement the `todo!()` functions until `cargo test -p <package>` is green!

## Syllabus

| # | Module | Package Name | Core Concepts |
| --- | --- | --- | --- |
| 01 | [Basics](./01-basics/README.md) | `lesson-01-basics` | `let` / `mut`, scalar & compound types, expressions, `if`, loops |
| 02 | [Ownership & Borrowing](./02-ownership-and-borrowing/README.md) | `lesson-02-ownership` | Move semantics, references (`&T`, `&mut T`), slices (`&str`, `&[T]`) |
| 03 | [Structs, Enums & Matching](./03-structs-enums-matching/README.md) | `lesson-03-types` | `struct`, `impl`, `enum` with data, `Option<T>`, `match` |
| 04 | [Error Handling & Collections](./04-error-handling-and-collections/README.md) | `lesson-04-errors` | `Vec`, `HashMap`, `Result<T, E>`, `?` operator, custom errors |
| 05 | [Mini Project: CLI Task Tracker](./05-mini-project/README.md) | `lesson-05-todo-cli` | File I/O, CLI arg parsing, structs/enums/results combined |

## Quick `cargo` Cheat Sheet

```bash
cargo check                     # Fast compile check across all lessons
cargo test                      # Run all non-ignored tests in the workspace
cargo run -p lesson-05-todo-cli -- --help
cargo clippy                    # Helpful Rust linter suggestions
```
