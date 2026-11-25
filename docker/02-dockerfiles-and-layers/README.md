# Module 02: Dockerfiles & Layers

## How Images Are Built

A `Dockerfile` is a recipe of instructions (`FROM`, `WORKDIR`, `COPY`, `RUN`, `CMD`). Each instruction creates a **cached layer**:

- Layers that haven't changed are reused instantly on rebuilds.
- Put **slow, rarely changing steps first** (e.g., installing dependencies) and **frequently changing files last** (e.g., `COPY . .`).
- Always include a `.dockerignore` file so `.git`, `node_modules`, `target/`, or local secrets aren't sent to the Docker build context.

## Hands-On Lab

Run these commands from `docker/02-dockerfiles-and-layers`:

### 1. Inspect the files

Read [`Dockerfile`](./Dockerfile), [`.dockerignore`](./.dockerignore), and [`app.py`](./app.py).

### 2. Build the image

```bash
docker build -t mini-hello:1.0 .
```

### 3. Run your custom image

```bash
docker run --rm -p 8000:8000 -e APP_MESSAGE="Built from my own Dockerfile!" mini-hello:1.0
```

Visit `http://localhost:8000` (or run `curl http://localhost:8000` in another terminal). Press `Ctrl+C` to stop.

### 4. Observe layer caching

Run `docker build -t mini-hello:1.0 .` a second time — notice every layer says `CACHED` and finishes in milliseconds!

## Try It Yourself

1. Edit `app.py` to add a `"version": "1.1"` field to the JSON response.
2. Rebuild as `mini-hello:1.1` and run it to verify the change.
3. Check the image size with `docker images mini-hello`.
4. (Bonus) Look up **multi-stage builds** (`FROM rust:1.82 AS builder` → `FROM debian:bookworm-slim`): they let you compile with a huge SDK image and ship only a tiny binary in the final image.

---

Next: [Module 03 — Volumes & Networking](../03-volumes-and-networking/README.md)
