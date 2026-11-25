# Module 05: Mini Project — Visit Counter API

Combine everything from Modules 01–04 by building and running a **2-tier Visit Counter API** with zero external Python packages:

- **`api`**: Custom Python HTTP server built from [`Dockerfile`](./Dockerfile) that talks to Redis over Docker's internal network (`redis:6379`).
- **`redis`**: Redis 7 with a named volume (`redis-data`) so visit counts survive restarts.

```text
[Browser / curl] --:8000--> [api container] --redis:6379--> [redis container] --> [volume: redis-data]
```

## Hands-On Walkthrough

Run these commands from `docker/05-mini-project`:

### 1. Build and start the stack

```bash
docker compose up -d --build
docker compose ps
```

### 2. Hit the API multiple times

```bash
curl http://localhost:8000
curl http://localhost:8000
curl http://localhost:8000
```

Watch the `"visits"` counter increment on every request!

### 3. Verify persistence across restarts

```bash
docker compose restart
curl http://localhost:8000
```

The counter continues from where it left off because Redis stores data in the `redis-data` named volume.

### 4. Clean up

```bash
docker compose down -v
```

## Final Challenges

1. **Add a `/reset` endpoint** in [`app.py`](./app.py) that sends `DEL visits` to Redis and returns `{"visits": 0}`, then rebuild with `docker compose up -d --build`.
2. **Add a `healthcheck`** to the `api` service in [`compose.yaml`](./compose.yaml) that checks `http://localhost:8000/health`.
3. **Add a `.dockerignore`** file so unnecessary files aren't copied into the image build context.

---

Congratulations! You now know the essential Docker workflow used across local dev, CI/CD, and production containers.
