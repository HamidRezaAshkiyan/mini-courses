# AGENTS.md — mini-courses

## Overview
A multi-topic collection of bite-sized, hands-on developer mini courses (~1–3 hours each) covering **Design Patterns**, **Docker**, **Kubernetes**, and **Rust**. Every course follows a consistent 5-module progression (4 concept modules + 1 capstone mini-project) with runnable demos, manifests, and unit-tested exercises.

## Tech Stack & Requirements
- **Design Patterns (`design-patterns/`)**: Python 3.10+ (standard library only: `abc`, `dataclasses`, `unittest`)
- **Rust Basics (`rust/`)**: Rust 2021 edition Cargo workspace (`resolver = "2"`), zero external crate dependencies
- **Docker Basics (`docker/`)**: Docker CLI + Docker Compose v2 (Python + Nginx + Redis examples)
- **Kubernetes Basics (`kubernetes/`)**: `kubectl` + local K8s cluster (Docker Desktop, `kind`, `minikube`, or Killercoda)

## Repository Structure
```text
mini-courses/
├── README.md                                # Top-level course index
├── COURSE_TEMPLATE.md                       # Standard blueprint for authoring new courses
├── design-patterns/                         # 5 Python modules (demo.py + exercise.py per module)
│   ├── 01-strategy-and-factory/
│   ├── 02-builder-and-singleton/
│   ├── 03-adapter-and-decorator/
│   ├── 04-observer-and-command/
│   └── 05-mini-project/                     # order_pipeline.py + test_order_pipeline.py
├── docker/                                  # 5 Docker modules (Dockerfiles, compose.yaml, app.py)
│   ├── 01-images-and-containers/
│   ├── 02-dockerfiles-and-layers/
│   ├── 03-volumes-and-networking/
│   ├── 04-docker-compose/
│   └── 05-mini-project/                     # 2-tier Python + Redis Visit Counter API
├── kubernetes/                              # 5 Kubernetes modules (declarative YAML manifests)
│   ├── 01-containers-and-pods/
│   ├── 02-deployments-and-scaling/
│   ├── 03-services-and-networking/
│   ├── 04-configmaps-and-secrets/
│   └── 05-mini-project/                     # namespace.yaml, redis.yaml, web.yaml
└── rust/                                    # Cargo workspace (5 zero-dependency crates)
    ├── Cargo.toml                           # Workspace manifest
    ├── SYNTAX_AND_CSHARP_GUIDE.md           # Quick-start guide for C#/Java/TS developers
    ├── 01-basics/                           # Package: lesson-01-basics
    ├── 02-ownership-and-borrowing/          # Package: lesson-02-ownership
    ├── 03-structs-enums-matching/           # Package: lesson-03-types
    ├── 04-error-handling-and-collections/   # Package: lesson-04-errors
    └── 05-mini-project/                     # Package: lesson-05-todo-cli
```

## Architecture & Key Flows
- **Course Structure**: Each top-level course directory has a `README.md` syllabus and numbered modules `01-*` through `05-mini-project`.
- **Exercise Pattern**:
  - **Design Patterns**: Each module provides a runnable `demo.py` and an `exercise.py` containing `NotImplementedError` stubs paired with `@unittest.skip(...)` tests. Learners remove `@unittest.skip` and implement the stubs.
  - **Rust**: Each module crate contains a runnable `src/main.rs` demo plus passing example tests and `#[ignore]`d exercise tests backed by `todo!()` stubs.
  - **Docker / Kubernetes**: Declarative `Dockerfile`, `compose.yaml`, and K8s YAML manifests applied incrementally per module.

## Development & Commands
- **Design Patterns (Python)**:
  ```bash
  python3 design-patterns/01-strategy-and-factory/demo.py
  python3 -m unittest design-patterns/01-strategy-and-factory/exercise.py
  python3 -m unittest design-patterns/05-mini-project/test_order_pipeline.py
  ```
- **Rust (run inside `rust/`)**:
  ```bash
  cd rust
  cargo check
  cargo test                                 # Non-ignored example tests
  cargo run -p lesson-01-basics              # Run module demo
  cargo test -p lesson-01-basics -- --ignored # Run exercise tests
  cargo clippy
  ```
- **Docker**:
  ```bash
  cd docker/05-mini-project && docker compose up -d --build
  docker compose down -v
  ```
- **Kubernetes**:
  ```bash
  kubectl apply -f kubernetes/05-mini-project/
  kubectl delete -f kubernetes/05-mini-project/
  ```

## Configuration & Environment
- No external API keys or real secrets are used.
- `kubernetes/04-configmaps-and-secrets/secret.yaml` contains intentionally dummy example credentials for learning Kubernetes `Secret` mechanics — never put real secrets there.

## Conventions & Gotchas
- **Preserve learner stubs**: Unless explicitly asked to solve exercises, keep `@unittest.skip` / `NotImplementedError` (Python) and `#[ignore]` / `todo!()` (Rust) intact so the repo remains usable as a self-paced course.
- **Zero-dependency rule**: Both `design-patterns/` (Python) and `rust/` (Cargo workspace) intentionally use zero external packages so learners can run everything offline without setup friction.
- **Adding a new course**: Follow `COURSE_TEMPLATE.md` (4–5 numbered modules + final mini-project) and register the course in the root `README.md` table.
- **Rust package names vs folder names**: Note that `rust/` package names (`lesson-02-ownership`, `lesson-03-types`, `lesson-04-errors`, `lesson-05-todo-cli`) are shorter than their directory names (`02-ownership-and-borrowing`, etc.).
