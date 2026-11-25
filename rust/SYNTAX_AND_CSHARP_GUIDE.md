# Rust Syntax at a Glance (and How It Compares to C#)

If you already know **C#** (or Java / TypeScript), this 5-minute guide maps Rust's syntax and mental model to concepts you already use every day.

---

## Part 1: Simple Rust Syntax Explained

### Variables & Mutability
```rust
let name = "Hamid";       // Immutable by default (cannot be reassigned)
let mut count = 0;        // Opt-in mutability with `mut`
count += 1;

const MAX_RETRIES: u32 = 3; // Compile-time constant (type required)
```

### Common Types
| Rust | Meaning |
| --- | --- |
| `i32`, `i64` | Signed integers (32-bit, 64-bit) |
| `u32`, `usize` | Unsigned integers (`usize` is used for lengths & array indexes) |
| `f64` | 64-bit floating point (`double` in C#) |
| `bool` | `true` / `false` |
| `&str` | Borrowed string slice (read-only view, like a string literal `"hi"`) |
| `String` | Owned, growable heap string (`String::from("hi")`) |
| `Vec<T>` | Growable list (`List<T>` in C#) |

### Functions & Return Values
```rust
// Parameters always have explicit types; return type follows `->`
fn add(a: i32, b: i32) -> i32 {
    a + b // No semicolon = implicit return! (`return a + b;` also works)
}
```

### Control Flow (`if`, `for`, `match`)
```rust
// `if` doesn't need parentheses and can return a value
let status = if count > 0 { "active" } else { "empty" };

// `for` over ranges (`0..5` is 0..4, `0..=5` is 0..5)
for i in 0..5 {
    println!("{i}"); // Macros end with `!`
}

// `match` is an exhaustive switch expression
match count {
    0 => println!("none"),
    1..=5 => println!("a few"),
    _ => println!("many"), // `_` is the wildcard / default arm
}
```

### Structs, Methods & Traits
Data (`struct`) and behavior (`impl`) are declared separately:

```rust
struct User {
    name: String,
    age: u32,
}

impl User {
    // Associated function (like a static factory method): called as `User::new(...)`
    fn new(name: &str, age: u32) -> Self {
        Self {
            name: name.to_string(),
            age,
        }
    }

    // Instance method borrowing self immutably (`&self`)
    fn greet(&self) -> String {
        format!("Hi, I'm {}", self.name)
    }
}
```

### Macros (`!`)
Anything ending in `!` (like `println!`, `format!`, `vec!`, `todo!`) is a **macro**, not a regular function. Macros expand at compile time, which is how `println!` can accept a variable number of arguments and type-check format strings at compile time.

---

## Part 2: Rust vs C# — Key Differences

### Quick Comparison Table

| Concept | C# | Rust |
| --- | --- | --- |
| **Memory management** | Garbage Collector (GC) | **Ownership & Borrowing** checked at compile time (no GC) |
| **Mutability** | Mutable by default (`readonly` to lock) | Immutable by default (`mut` to unlock) |
| **Nullability** | `null` / nullable refs (`User?`) | No `null` — uses `Option<T>` (`Some(v)` / `None`) |
| **Error handling** | Exceptions (`try` / `catch` / `throw`) | Return values: `Result<T, E>` + `?` operator |
| **OOP / Polymorphism** | `class`, inheritance, `interface` | `struct` + `enum` + `trait` (composition over inheritance) |
| **Strings** | `string` (immutable GC reference) | `String` (owned, mutable) vs `&str` (borrowed slice) |
| **Collections** | `List<T>`, `Dictionary<K, V>` | `Vec<T>`, `HashMap<K, V>` |
| **Functional queries** | LINQ (`.Where().Select().ToList()`) | Iterators (`.iter().filter().map().collect()`) |
| **Package manager** | `dotnet` / NuGet (`.csproj`) | `cargo` / crates.io (`Cargo.toml`) |
| **Runtime** | .NET CLR (JIT / AOT) | Native binary (no runtime) |

---

### Side-by-Side Examples

#### 1. No `null` — `Option<T>` instead

**C#:**
```csharp
User? FindUser(int id) => id == 1 ? new User("Alice") : null;

var user = FindUser(1);
Console.WriteLine(user?.Name ?? "Guest");
```

**Rust:**
```rust
fn find_user(id: u32) -> Option<String> {
    if id == 1 { Some("Alice".to_string()) } else { None }
}

let user = find_user(1);
println!("{}", user.as_deref().unwrap_or("Guest"));
```

#### 2. No Exceptions — `Result<T, E>` and `?` instead

**C#:**
```csharp
int ParseDouble(string text) {
    int n = int.Parse(text); // throws FormatException on failure
    return n * 2;
}
```

**Rust:**
```rust
fn parse_double(text: &str) -> Result<i32, std::num::ParseIntError> {
    let n: i32 = text.parse()?; // `?` returns `Err` early if parsing fails
    Ok(n * 2)
}
```

#### 3. Interfaces vs Traits (Composition, No Class Inheritance)

Rust does **not** have `class` inheritance (`class Dog : Animal`). Instead, you share behavior using **traits** (very similar to C# `interface`s, except you can even implement a trait for an existing type):

**C#:**
```csharp
interface ISpeak {
    string Speak();
}

class Dog : ISpeak {
    public string Speak() => "Woof!";
}
```

**Rust:**
```rust
trait Speak {
    fn speak(&self) -> &'static str;
}

struct Dog;

impl Speak for Dog {
    fn speak(&self) -> &'static str {
        "Woof!"
    }
}
```

#### 4. LINQ vs Rust Iterators

Both are **lazy** (nothing runs until consumed by `.ToList()` / `.collect()`):

**C#:**
```csharp
var evens = numbers
    .Where(n => n % 2 == 0)
    .Select(n => n * 10)
    .ToList();
```

**Rust:**
```rust
let evens: Vec<i32> = numbers
    .iter()
    .filter(|&&n| n % 2 == 0)
    .map(|&n| n * 10)
    .collect();
```

#### 5. The Biggest Mindset Shift: Ownership vs Garbage Collection

In **C#**, passing an object to a function copies a reference, and the GC cleans it up later whenever nobody points to it anymore:
```csharp
var name = "Alice"; // or a List<int>
PrintList(myList);
// `myList` is still usable here
```

In **Rust**, heap values like `String` or `Vec<T>` have **one owner**. Passing by value **moves** ownership; passing by reference (`&`) **borrows** it:
```rust
let names = vec!["Alice", "Bob"];
print_list(&names); // Borrow with `&` so `names` stays usable here!
println!("Still have {} names", names.len());
```

If you forget `&` and pass `names` by value, the Rust compiler stops you at compile time — preventing use-after-free, data races, and null reference exceptions before your program ever runs.

---

Ready to practice? Head back to the [Rust Course README](./README.md) and start [Module 01](./01-basics/README.md)!
