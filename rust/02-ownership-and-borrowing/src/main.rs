fn main() {
    // 1. Move semantics
    let s1 = String::from("hello");
    let s2 = s1; // s1 is moved into s2; s1 can no longer be used
    println!("Moved string: {s2}");

    // 2. Immutable borrowing (&T)
    let len = count_chars(&s2);
    println!("'{s2}' has {len} chars (still owned by s2!)");

    // 3. Mutable borrowing (&mut T)
    let mut greeting = String::from("Hi");
    add_name(&mut greeting, "Rustacean");
    println!("Mutated greeting: {greeting}");

    // 4. Slices (&[i32])
    let numbers = vec![10, 20, 30, 40];
    println!("Sum of middle slice: {}", sum_slice(&numbers[1..3]));
}

fn count_chars(s: &str) -> usize {
    s.chars().count()
}

fn add_name(target: &mut String, name: &str) {
    target.push_str(", ");
    target.push_str(name);
}

pub fn sum_slice(nums: &[i32]) -> i32 {
    nums.iter().sum()
}

// ============================================================================
// Hands-On Exercises
// Remove `#[ignore]` from the tests below and replace `todo!()` with your code.
// ============================================================================

/// Exercise 1: Return the first space-delimited word as a string slice (`&str`).
/// Hint: `s.find(' ')` or `s.split_whitespace().next()`.
pub fn first_word(_s: &str) -> &str {
    todo!("Return the first word slice without allocating a new String")
}

/// Exercise 2: Append "!" to the end of `s` only if it does not already end with '!'.
pub fn append_exclamation(_s: &mut String) {
    todo!("Mutate the borrowed String in place")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_sum_slice() {
        let data = [1, 2, 3, 4];
        assert_eq!(sum_slice(&data), 10);
        assert_eq!(sum_slice(&data[1..3]), 5);
    }

    #[test]
    #[ignore = "Hands-on exercise: remove #[ignore] and implement first_word"]
    fn exercise_first_word() {
        assert_eq!(first_word("hello world"), "hello");
        assert_eq!(first_word("rust"), "rust");
        assert_eq!(first_word(""), "");
    }

    #[test]
    #[ignore = "Hands-on exercise: remove #[ignore] and implement append_exclamation"]
    fn exercise_append_exclamation() {
        let mut s = String::from("wow");
        append_exclamation(&mut s);
        assert_eq!(s, "wow!");
        append_exclamation(&mut s);
        assert_eq!(s, "wow!");
    }
}
