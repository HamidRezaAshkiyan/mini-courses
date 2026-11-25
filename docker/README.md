# Docker Basics — Mini Course

Learn how to package, run, connect, and compose containerized applications using Docker and Docker Compose.

## Prerequisites

- Docker installed (Docker Desktop, OrbStack, or Colima + Docker CLI)
- Verify Docker is running:
  ```bash
  docker --version
  docker compose version
  docker run --rm hello-world
  ```

## Syllabus

| # | Module | Core Concepts |
| --- | --- | --- |
| 01 | [Images & Containers](./01-images-and-containers/README.md) | Image vs container, `run`, `ps`, `logs`, `exec`, `-p` ports, `-e` env vars |
| 02 | [Dockerfiles & Layers](./02-dockerfiles-and-layers/README.md) | Writing a `Dockerfile`, layer caching, `.dockerignore`, multi-stage builds |
| 03 | [Volumes & Networking](./03-volumes-and-networking/README.md) | Bind mounts vs named volumes, custom bridge networks & DNS |
| 04 | [Docker Compose](./04-docker-compose/README.md) | Multi-container stacks with `compose.yaml`, `depends_on`, healthchecks |
| 05 | [Mini Project: Visit Counter API](./05-mini-project/README.md) | Build and run a 2-tier Python + Redis app with Compose |

## Quick `docker` Cheat Sheet

```bash
# Run & manage containers
docker run -d --name web -p 8080:80 nginx:1.27-alpine
docker ps -a
docker logs -f web
docker exec -it web sh
docker rm -f web

# Build & inspect images
docker build -t my-app:1.0 .
docker images

# Docker Compose
docker compose up -d --build
docker compose logs -f
docker compose down -v
```
