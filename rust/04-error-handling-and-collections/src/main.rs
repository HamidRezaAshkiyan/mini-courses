use std::collections::HashMap;
use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub enum MathError {
    DivisionByZero,
}

pub fn safe_divide(a: f64, b: f64) -> Result<f64, MathError> {
    if b == 0.0 {
        Err(MathError::DivisionByZero)
    } else {
        Ok(a / b)
    }
}

fn main() {
    // 1. Handling Result with match
    for (a, b) in [(10.0, 2.0), (5.0, 0.0)] {
        match safe_divide(a, b) {
            Ok(result) => println!("{a} / {b} = {result}"),
            Err(err) => println!("{a} / {b} failed: {err:?}"),
        }
    }

    // 2. Vec + iterator pipeline
    let numbers = vec![1, 2, 3, 4, 5, 6];
    let doubled_evens: Vec<i32> = numbers
        .iter()
        .filter(|&&n| n % 2 == 0)
        .map(|&n| n * 2)
        .collect();
    println!("Doubled evens: {doubled_evens:?}");

    // 3. HashMap entry API
    let mut scores: HashMap<&str, i32> = HashMap::new();
    scores.insert("Alice", 10);
    *scores.entry("Bob").or_insert(0) += 5;
    println!("Scores: {scores:?}");
}

// ============================================================================
// Hands-On Exercises
// Remove `#[ignore]` from the tests below and replace `todo!()` with your code.
// ============================================================================

/// Exercise 1: Parse every string in `lines` as an `i32` and return their sum.
/// Use the `?` operator to propagate any `ParseIntError`.
pub fn parse_and_sum(_lines: &[&str]) -> Result<i32, ParseIntError> {
    todo!("Parse each trimmed &str into i32 using `?` and accumulate the sum")
}

/// Exercise 2: Count occurrences of each whitespace-separated word (lowercased).
pub fn word_counts(_text: &str) -> HashMap<String, usize> {
    todo!("Use split_whitespace(), to_lowercase(), and HashMap::entry()")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_safe_divide() {
        assert_eq!(safe_divide(10.0, 2.0), Ok(5.0));
        assert_eq!(safe_divide(10.0, 0.0), Err(MathError::DivisionByZero));
    }

    #[test]
    #[ignore = "Hands-on exercise: remove #[ignore] and implement parse_and_sum"]
    fn exercise_parse_and_sum() {
        assert_eq!(parse_and_sum(&["10", "20", "-5"]), Ok(25));
        assert_eq!(parse_and_sum(&[]), Ok(0));
        assert!(parse_and_sum(&["10", "oops"]).is_err());
    }

    #[test]
    #[ignore = "Hands-on exercise: remove #[ignore] and implement word_counts"]
    fn exercise_word_counts() {
        let counts = word_counts("Rust is fast and rust is fun");
        assert_eq!(counts.get("rust"), Some(&2));
        assert_eq!(counts.get("is"), Some(&2));
        assert_eq!(counts.get("fast"), Some(&1));
        assert_eq!(counts.get("python"), None);
    }
}
