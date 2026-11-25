# Module 03: Volumes & Networking

## Persistence: Bind Mounts vs Named Volumes

Because containers are ephemeral, Docker gives you two ways to keep data outside the container's writable layer:

| Type | Syntax | Best For |
| --- | --- | --- |
| **Bind Mount** | `-v "$(pwd):/path/in/container"` | Local development (live-editing files on your laptop) |
| **Named Volume** | `-v my-data:/var/lib/data` | Databases & persistent state managed by Docker |

## Networking: Custom Bridge Networks & DNS

When two containers join the **same user-defined bridge network**, Docker provides automatic **DNS resolution by container name** (e.g., `redis`, `db`, `api`) — no IP addresses needed.

## Hands-On Lab

Run these commands from `docker/03-volumes-and-networking`:

### 1. Bind mount a local HTML file into Nginx

```bash
docker run -d --name live-site \
  -p 8080:80 \
  -v "$(pwd)/index.html:/usr/share/nginx/html/index.html:ro" \
  nginx:1.27-alpine
```

Open `http://localhost:8080`. Now edit [`index.html`](./index.html) and refresh the browser — your change appears immediately without rebuilding!

Clean up:
```bash
docker rm -f live-site
```

### 2. Test a named volume surviving container deletion

```bash
# Write a file into a named volume
docker run --rm -v demo-vol:/data alpine:3.20 sh -c 'echo "persisted!" > /data/note.txt'

# Read it back from a brand-new container
docker run --rm -v demo-vol:/data alpine:3.20 cat /data/note.txt

# Remove the volume when finished
docker volume rm demo-vol
```

### 3. Connect two containers over a custom network

```bash
docker network create mini-net
docker run -d --name cache --network mini-net redis:7-alpine
docker run --rm --network mini-net redis:7-alpine redis-cli -h cache ping
# Expected output: PONG
```

Notice `-h cache` resolved automatically via Docker's embedded DNS!

Clean up:
```bash
docker rm -f cache
docker network rm mini-net
```

---

Next: [Module 04 — Docker Compose](../04-docker-compose/README.md)
