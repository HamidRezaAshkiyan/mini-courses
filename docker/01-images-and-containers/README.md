# Module 01: Images & Containers

## Core Concepts

- **Image:** A read-only template containing your app, runtime, libraries, and default startup command (like a class or snapshot).
- **Container:** A running (or stopped) isolated instance of an image with its own thin writable layer (like an object instance).
- Containers are **ephemeral** — anything written inside a container's filesystem disappears when the container is removed (we'll solve persistence with Volumes in Module 03).

## Hands-On Lab

### 1. Run Nginx in the background with port mapping

```bash
docker run -d --name my-nginx -p 8080:80 nginx:1.27-alpine
```

- `-d` runs detached (in the background).
- `--name my-nginx` gives it a readable name.
- `-p 8080:80` maps port `8080` on your machine → port `80` inside the container.

Open `http://localhost:8080` (or run `curl http://localhost:8080`).

### 2. Inspect, view logs, and shell into the container

```bash
docker ps
docker logs my-nginx
docker exec -it my-nginx sh -c "nginx -v && ls /usr/share/nginx/html"
```

### 3. Pass environment variables (`-e`)

```bash
docker run --rm -e GREETING="Hello Docker!" alpine:3.20 sh -c 'echo "$GREETING"'
```

Notice `--rm` automatically deletes the container when it exits — great for one-off commands.

## Try It Yourself

1. Start a second Nginx container named `my-nginx-2` mapped to port `8081` on your host.
2. Verify both `http://localhost:8080` and `http://localhost:8081` respond.
3. Clean up both containers:
   ```bash
   docker rm -f my-nginx my-nginx-2
   ```

---

Next: [Module 02 — Dockerfiles & Layers](../02-dockerfiles-and-layers/README.md)
