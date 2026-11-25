# Module 01: Containers & Pods

## Why Pods Exist

Kubernetes does not run bare containers directly — it wraps one or more containers in a **Pod**.

- A **Pod** is the smallest deployable unit in Kubernetes.
- All containers in a Pod share the same **IP address**, **network namespace** (they talk over `localhost`), and optional shared **volumes**.
- Pods are **ephemeral**: if a Pod dies, Kubernetes does not resurrect that exact Pod (that's what Deployments are for in Module 02).

## Anatomy of a Manifest

Every Kubernetes YAML file has 4 top-level fields:

| Field | Meaning |
| --- | --- |
| `apiVersion` | Which Kubernetes API group/version defines this resource (`v1` for Pods) |
| `kind` | The resource type (`Pod`, `Deployment`, `Service`, etc.) |
| `metadata` | Name, namespace, and key-value `labels` |
| `spec` | The desired state (which container image, ports, etc.) |

Open [`pod.yaml`](./pod.yaml) and read through it before running anything.

## Hands-On Lab

Run these commands from the `kubernetes/01-containers-and-pods` directory:

### 1. Create the Pod

```bash
kubectl apply -f pod.yaml
```

### 2. Watch it start and inspect it

```bash
kubectl get pods
kubectl describe pod hello-nginx
```

### 3. View logs and open a shell inside the container

```bash
kubectl logs hello-nginx
kubectl exec -it hello-nginx -- sh -c "nginx -v && hostname"
```

### 4. Test it from your machine

```bash
kubectl port-forward pod/hello-nginx 8080:80
```

Open `http://localhost:8080` in your browser (or run `curl http://localhost:8080` in another terminal). Press `Ctrl+C` to stop port-forwarding.

## Try It Yourself

1. Edit `pod.yaml` to add a new label `env: learning` under `metadata.labels`, then re-apply it.
2. Verify the label shows up with:
   ```bash
   kubectl get pods --show-labels
   ```
3. Delete the Pod and confirm it is **not** recreated automatically:
   ```bash
   kubectl delete -f pod.yaml
   kubectl get pods
   ```

---

Next: [Module 02 — Deployments & Scaling](../02-deployments-and-scaling/README.md)
