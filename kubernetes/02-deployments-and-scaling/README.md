# Module 02: Deployments & Scaling

## Why Deployments Exist

In Module 01, deleting a Pod meant it was gone forever. In production, you want Kubernetes to:

1. Keep `N` copies (replicas) running at all times (**self-healing**).
2. Scale up or down with a single change.
3. Roll out new image versions with zero downtime — and **roll back** if something breaks.

A **Deployment** manages a **ReplicaSet**, which manages your **Pods**:

```text
Deployment  ──▶  ReplicaSet  ──▶  Pod 1, Pod 2, Pod 3
```

## Hands-On Lab

Run these commands from `kubernetes/02-deployments-and-scaling`:

### 1. Deploy 3 replicas

```bash
kubectl apply -f deployment.yaml
kubectl get deployments,replicasets,pods
```

### 2. Test self-healing

Pick one of the Pod names from `kubectl get pods` and delete it:

```bash
kubectl delete pod <pod-name>
kubectl get pods
```

Notice that Kubernetes immediately spins up a replacement Pod to maintain `replicas: 3`.

### 3. Scale up and down

```bash
kubectl scale deployment web-app --replicas=5
kubectl get pods -l app=web-app

kubectl scale deployment web-app --replicas=2
kubectl get pods -l app=web-app
```

### 4. Perform a rolling update and rollback

```bash
# Update the container image
kubectl set image deployment/web-app nginx=nginx:1.27.3-alpine

# Watch the rollout progress
kubectl rollout status deployment/web-app

# Inspect rollout history
kubectl rollout history deployment/web-app

# Roll back to the previous revision
kubectl rollout undo deployment/web-app
```

## Try It Yourself

1. Intentionally break the deployment with a non-existent image tag (`nginx:does-not-exist`) using `kubectl set image`.
2. Run `kubectl get pods` and `kubectl describe pod <new-pod>` to see `ImagePullBackOff` — notice the old healthy Pods stay alive!
3. Fix it using `kubectl rollout undo deployment/web-app`.
4. Clean up when done:
   ```bash
   kubectl delete -f deployment.yaml
   ```

---

Next: [Module 03 — Services & Networking](../03-services-and-networking/README.md)
