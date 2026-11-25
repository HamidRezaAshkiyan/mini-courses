use std::f64::consts::PI;

#[derive(Debug, PartialEq)]
pub struct Rectangle {
    pub width: f64,
    pub height: f64,
}

impl Rectangle {
    pub fn new(width: f64, height: f64) -> Self {
        Self { width, height }
    }

    pub fn perimeter(&self) -> f64 {
        2.0 * (self.width + self.height)
    }
}

#[derive(Debug)]
pub enum Shape {
    Circle { radius: f64 },
    Rectangle(Rectangle),
}

impl Shape {
    /// Exercise 1: Compute the area of any `Shape` using `match`.
    /// Circle area = PI * radius * radius
    /// Rectangle area = width * height
    pub fn area(&self) -> f64 {
        let _ = PI;
        todo!("Match on self to compute area for Circle and Rectangle")
    }
}

fn describe_option(value: Option<i32>) -> String {
    match value {
        Some(n) if n > 0 => format!("positive number: {n}"),
        Some(n) => format!("non-positive number: {n}"),
        None => String::from("nothing here"),
    }
}

/// Exercise 2: Return the first negative number in `nums`, or `None` if all are >= 0.
pub fn find_first_negative(_nums: &[i32]) -> Option<i32> {
    todo!("Iterate over nums and return Some(n) for the first n < 0, else None")
}

fn main() {
    let rect = Rectangle::new(4.0, 6.0);
    println!("Rect: {rect:?}, perimeter = {}", rect.perimeter());

    println!("{}", describe_option(Some(42)));
    println!("{}", describe_option(None));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_rectangle_perimeter() {
        let rect = Rectangle::new(3.0, 5.0);
        assert_eq!(rect.perimeter(), 16.0);
    }

    #[test]
    #[ignore = "Hands-on exercise: remove #[ignore] and implement Shape::area"]
    fn exercise_shape_area() {
        let circle = Shape::Circle { radius: 2.0 };
        let rect = Shape::Rectangle(Rectangle::new(3.0, 4.0));

        assert!((circle.area() - (PI * 4.0)).abs() < 1e-9);
        assert!((rect.area() - 12.0).abs() < 1e-9);
    }

    #[test]
    #[ignore = "Hands-on exercise: remove #[ignore] and implement find_first_negative"]
    fn exercise_find_first_negative() {
        assert_eq!(find_first_negative(&[3, 0, -4, -9]), Some(-4));
        assert_eq!(find_first_negative(&[1, 2, 3]), None);
        assert_eq!(find_first_negative(&[]), None);
    }
}
