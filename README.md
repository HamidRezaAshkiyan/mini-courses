# Mini Courses

A growing collection of bite-sized, hands-on mini courses designed to teach the core fundamentals of developer tools, languages, and infrastructure — fast, practical, and without fluff.

Each course takes roughly **1–3 hours** to complete and combines concise explanations with runnable code or manifests you can experiment with locally.

## Courses

| Course | Level | Modules | What You'll Build / Do |
| --- | --- | --- | --- |
| [Kubernetes Basics](./kubernetes/README.md) | Beginner | 5 | Deploy pods, scale deployments, expose services, inject config/secrets, and run a 2-tier app |
| [Rust Basics](./rust/README.md) | Beginner | 5 | Master ownership, structs/enums, error handling, and build a zero-dependency CLI task tracker |

## How to Use This Repo

1. Clone the repository:
   ```bash
   git clone https://github.com/HamidRezaAshkiyan/mini-courses.git
   cd mini-courses
   ```
2. Pick a course folder and start with its `README.md`.
3. Work through the numbered modules in order (`01-*`, `02-*`, ...).
4. Do the **Hands-On Lab / Exercise** at the end of every module — reading alone won't stick.

## Adding a New Course

This repository is structured to grow over time. To add a new mini course:

1. Create a new top-level folder (e.g., `docker/`, `go/`, `postgres/`).
2. Follow the layout in [`COURSE_TEMPLATE.md`](./COURSE_TEMPLATE.md) (4–5 short modules + a final mini-project).
3. Add a row to the **Courses** table above.
