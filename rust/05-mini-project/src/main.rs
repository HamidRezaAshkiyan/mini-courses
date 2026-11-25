use std::env;
use std::fs;
use std::io;
use std::path::Path;
use std::process;

const DEFAULT_DB: &str = "tasks.txt";

#[derive(Debug, PartialEq)]
pub struct Task {
    pub done: bool,
    pub title: String,
}

impl Task {
    pub fn new(title: impl Into<String>) -> Self {
        Self {
            done: false,
            title: title.into(),
        }
    }

    pub fn serialize(&self) -> String {
        let marker = if self.done { "x" } else { " " };
        format!("[{marker}] {}", self.title)
    }

    pub fn parse(line: &str) -> Option<Self> {
        if let Some(rest) = line.strip_prefix("[x] ") {
            Some(Self {
                done: true,
                title: rest.to_string(),
            })
        } else if let Some(rest) = line.strip_prefix("[ ] ") {
            Some(Self {
                done: false,
                title: rest.to_string(),
            })
        } else {
            None
        }
    }
}

pub fn load_tasks(path: &Path) -> io::Result<Vec<Task>> {
    match fs::read_to_string(path) {
        Ok(content) => Ok(content.lines().filter_map(Task::parse).collect()),
        Err(err) if err.kind() == io::ErrorKind::NotFound => Ok(Vec::new()),
        Err(err) => Err(err),
    }
}

pub fn save_tasks(path: &Path, tasks: &[Task]) -> io::Result<()> {
    let body = tasks
        .iter()
        .map(Task::serialize)
        .collect::<Vec<_>>()
        .join("\n");
    fs::write(path, if body.is_empty() { body } else { format!("{body}\n") })
}

fn print_usage() {
    eprintln!(
        "Usage:
  todo add <task title>   Add a new task
  todo list               List all tasks
  todo done <number>      Mark a task as completed"
    );
}

fn run(args: &[String], db_path: &Path) -> Result<(), String> {
    let command = args.first().map(String::as_str).unwrap_or("help");

    match command {
        "add" => {
            let title = args[1..].join(" ").trim().to_string();
            if title.is_empty() {
                return Err("Please provide a task title.".to_string());
            }
            let mut tasks = load_tasks(db_path).map_err(|e| e.to_string())?;
            tasks.push(Task::new(&title));
            save_tasks(db_path, &tasks).map_err(|e| e.to_string())?;
            println!("Added: {title}");
            Ok(())
        }
        "list" => {
            let tasks = load_tasks(db_path).map_err(|e| e.to_string())?;
            if tasks.is_empty() {
                println!("No tasks yet! Add one with: add \"My first task\"");
            } else {
                for (idx, task) in tasks.iter().enumerate() {
                    println!("{}. {}", idx + 1, task.serialize());
                }
            }
            Ok(())
        }
        "done" => {
            let num_str = args
                .get(1)
                .ok_or_else(|| "Please provide a task number.".to_string())?;
            let index: usize = num_str
                .parse::<usize>()
                .map_err(|_| format!("'{num_str}' is not a valid task number."))?
                .checked_sub(1)
                .ok_or_else(|| "Task numbers start at 1.".to_string())?;

            let mut tasks = load_tasks(db_path).map_err(|e| e.to_string())?;
            let task = tasks
                .get_mut(index)
                .ok_or_else(|| format!("No task found at #{num_str}."))?;
            task.done = true;
            let title = task.title.clone();
            save_tasks(db_path, &tasks).map_err(|e| e.to_string())?;
            println!("Completed: {title}");
            Ok(())
        }
        "--help" | "-h" | "help" => {
            print_usage();
            Ok(())
        }
        other => Err(format!("Unknown command: '{other}'. Run with --help for usage.")),
    }
}

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();
    if let Err(err) = run(&args, Path::new(DEFAULT_DB)) {
        eprintln!("Error: {err}");
        process::exit(1);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn roundtrip_task_serialization() {
        let pending = Task::new("Learn Rust");
        assert_eq!(pending.serialize(), "[ ] Learn Rust");
        assert_eq!(Task::parse("[ ] Learn Rust"), Some(pending));

        let completed = Task {
            done: true,
            title: "Ship code".to_string(),
        };
        assert_eq!(completed.serialize(), "[x] Ship code");
        assert_eq!(Task::parse("[x] Ship code"), Some(completed));
    }

    #[test]
    fn parse_ignores_malformed_lines() {
        assert_eq!(Task::parse("not a valid line"), None);
        assert_eq!(Task::parse(""), None);
    }
}
