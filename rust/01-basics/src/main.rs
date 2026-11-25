fn main() {
    // 1. Immutability vs mutability
    let language = "Rust";
    let mut counter = 0;
    counter += 1;
    println!("Learning {language}! Counter = {counter}");

    // 2. Shadowing (even changing types)
    let spaces = "   ";
    let spaces = spaces.len();
    println!("Number of spaces: {spaces}");

    // 3. Expressions return values (notice: no semicolon on the last line)
    let score = 85;
    let grade = if score >= 90 {
        "A"
    } else if score >= 80 {
        "B"
    } else {
        "C"
    };
    println!("Score {score} => Grade {grade}");

    // 4. Loops & ranges
    let mut total = 0;
    for n in 1..=5 {
        total += n;
    }
    println!("Sum of 1..=5 = {total}");
}

/// Example function: returns `true` if `n` is divisible by 3 or 5.
pub fn is_fizz_or_buzz(n: u32) -> bool {
    n % 3 == 0 || n % 5 == 0
}

// ============================================================================
// Hands-On Exercises
// Remove `#[ignore]` from the tests below and replace `todo!()` with your code.
// ============================================================================

/// Exercise 1: Convert Celsius to Fahrenheit using `c * 9.0 / 5.0 + 32.0`.
pub fn celsius_to_fahrenheit(_c: f64) -> f64 {
    todo!("Implement Celsius to Fahrenheit conversion")
}

/// Exercise 2: Return the sum of all even numbers from 1 through `n` (inclusive).
pub fn sum_even_up_to(_n: u32) -> u32 {
    todo!("Sum all even integers in 1..=n")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_fizz_or_buzz() {
        assert!(is_fizz_or_buzz(3));
        assert!(is_fizz_or_buzz(10));
        assert!(!is_fizz_or_buzz(7));
    }

    #[test]
    #[ignore = "Hands-on exercise: remove #[ignore] and implement celsius_to_fahrenheit"]
    fn exercise_celsius_to_fahrenheit() {
        assert!((celsius_to_fahrenheit(0.0) - 32.0).abs() < 1e-9);
        assert!((celsius_to_fahrenheit(100.0) - 212.0).abs() < 1e-9);
    }

    #[test]
    #[ignore = "Hands-on exercise: remove #[ignore] and implement sum_even_up_to"]
    fn exercise_sum_even_up_to() {
        assert_eq!(sum_even_up_to(0), 0);
        assert_eq!(sum_even_up_to(6), 12); // 2 + 4 + 6
        assert_eq!(sum_even_up_to(7), 12);
    }
}
