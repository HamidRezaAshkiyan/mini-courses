# Module 04: Docker Compose

## Why Docker Compose?

Running `docker network create`, `docker volume create`, and multiple long `docker run` commands by hand gets painful fast.

**Docker Compose** lets you describe an entire multi-container stack (services, networks, volumes, ports, env vars, healthchecks) in a single declarative `compose.yaml` file and manage it with one command.

## Hands-On Lab

Run these commands from `docker/04-docker-compose`:

### 1. Start the stack

```bash
docker compose up -d
docker compose ps
```

### 2. Inspect logs and test Redis

```bash
docker compose logs
docker compose exec redis redis-cli ping
```

Visit `http://localhost:8080` to verify Nginx is serving traffic.

### 3. Stop and clean up

```bash
# Stop containers & remove the default network (keeps named volumes)
docker compose down

# Also remove named volumes
docker compose down -v
```

## Try It Yourself

1. Open [`compose.yaml`](./compose.yaml) and change Nginx's host port from `8080:80` to `8085:80`, then run `docker compose up -d` — Compose recreates only the service that changed!
2. Inspect the auto-created network with `docker network ls`.

---

Next: [Module 05 — Mini Project: Visit Counter API](../05-mini-project/README.md)
