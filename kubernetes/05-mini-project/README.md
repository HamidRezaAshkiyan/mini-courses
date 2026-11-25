# Module 05: Mini Project — Deploy a 2-Tier App

Put everything from Modules 01–04 together by deploying a tiny two-tier stack inside its own **Namespace**:

- **Namespace** (`k8s-mini-project`) to isolate all resources cleanly.
- **Redis** (`Deployment` + `ClusterIP Service`) as the backend store.
- **Web** (`ConfigMap` + `Deployment` + `ClusterIP Service`) serving a custom HTML page via Nginx and configured to know where Redis lives.

```text
[Your Laptop] --port-forward--> [Service: web] --> [2x Nginx Pods]
                                                      (knows REDIS_HOST=redis)
                                [Service: redis] --> [1x Redis Pod]
```

## Hands-On Walkthrough

Run these commands from `kubernetes/05-mini-project`:

### 1. Apply all manifests

```bash
kubectl apply -f namespace.yaml
kubectl apply -f redis.yaml
kubectl apply -f web.yaml
```

### 2. Inspect everything inside the namespace

```bash
kubectl get all -n k8s-mini-project
```

### 3. Verify Redis is reachable from the cluster

```bash
kubectl exec -n k8s-mini-project deploy/redis -- redis-cli ping
# Expected output: PONG
```

### 4. View the web app

```bash
kubectl port-forward -n k8s-mini-project svc/web 8080:80
```

Open `http://localhost:8080` in your browser!

## Final Challenges

1. **Customize the page:** Edit the `index.html` inside the `ConfigMap` in [`web.yaml`](./web.yaml), re-apply `web.yaml`, and refresh `http://localhost:8080`.
2. **Scale the web tier:** Scale `deploy/web` to 4 replicas in the `k8s-mini-project` namespace and confirm `kubectl get endpoints web -n k8s-mini-project` lists 4 IPs.
3. **Add a liveness probe:** Add a `livenessProbe` to the `web` container in `web.yaml` (checking `GET /` on port `80`) and re-apply.
4. **One-command cleanup:** Because everything lives in one namespace, deleting the namespace removes every resource inside it cleanly:
   ```bash
   kubectl delete namespace k8s-mini-project
   ```

---

Congratulations! You now know the core 20% of Kubernetes that covers 80% of day-to-day usage. Next topics to explore when ready: **Ingress**, **PersistentVolumeClaims (PVCs)**, **Helm**, and **RBAC**.
