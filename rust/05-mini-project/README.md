# Module 05: Mini Project — CLI Task Tracker

Combine structs, enums, `Result`, file I/O, and CLI argument parsing in a working zero-dependency CLI tool!

## Try It Out

From the `rust/` directory:

```bash
# Add tasks (saved to tasks.txt in the current directory)
cargo run -p lesson-05-todo-cli -- add "Learn Rust ownership"
cargo run -p lesson-05-todo-cli -- add "Deploy first K8s pod"

# List tasks
cargo run -p lesson-05-todo-cli -- list

# Mark task #1 as done
cargo run -p lesson-05-todo-cli -- done 1
cargo run -p lesson-05-todo-cli -- list

# Run unit tests
cargo test -p lesson-05-todo-cli
```

## Stretch Challenges (Hands-On Practice)

Once you've read through [`src/main.rs`](./src/main.rs), try extending it:

1. **Add a `remove <id>` command** that deletes a task by its 1-based index and saves the updated list.
2. **Add a `clear` command** that removes all completed tasks while keeping pending ones.
3. **Custom file path via env var:** Check `std::env::var("TODO_FILE")` and fall back to `"tasks.txt"` if unset.
4. **Add unit tests** for every new command you implement!

---

Congratulations! You've covered the essential foundations of Rust. Next topics to explore when ready: **Traits & Generics**, **Lifetimes**, **Cargo crates (`clap`, `serde`)**, and **Async Rust (`tokio`)**.
