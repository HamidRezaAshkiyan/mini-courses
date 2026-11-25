# Module 03: Services & Networking

## Why Services Exist

Pods come and go — every time a Pod is replaced, it gets a **new IP address**. You should never hardcode Pod IPs.

A **Service** gives a set of Pods:
- A **stable virtual IP** and **DNS name** (e.g., `web-app-svc.default.svc.cluster.local`, or simply `web-app-svc` inside the same namespace).
- Built-in **load balancing** across all healthy Pods matching its `selector`.

## Common Service Types

| Type | Reachable From | Typical Use |
| --- | --- | --- |
| `ClusterIP` (default) | Inside the cluster only | Internal APIs, databases, caches |
| `NodePort` | `<NodeIP>:<30000-32767>` | Local testing, simple external access |
| `LoadBalancer` | External cloud load balancer | Production ingress on cloud providers |

## Hands-On Lab

Run these commands from `kubernetes/03-services-and-networking`:

### 1. Start the Deployment from Module 02 + create the Service

```bash
kubectl apply -f ../02-deployments-and-scaling/deployment.yaml
kubectl apply -f service.yaml
```

### 2. Inspect the Service and its Endpoints

```bash
kubectl get svc web-app-svc
kubectl get endpoints web-app-svc
```

Notice `ENDPOINTS` lists the IP addresses of all 3 `web-app` Pods.

### 3. Test internal cluster DNS from a temporary Pod

```bash
kubectl run curl-test --rm -it --image=busybox:1.36 -- sh
```

Inside the shell, run:

```sh
nslookup web-app-svc
wget -qO- http://web-app-svc | head -n 5
exit
```

### 4. Access the Service from your machine

```bash
kubectl port-forward svc/web-app-svc 8080:80
```

Visit `http://localhost:8080`, then press `Ctrl+C`.

## Try It Yourself

1. Change `type: ClusterIP` in [`service.yaml`](./service.yaml) to `type: NodePort`, re-apply, and check the assigned port (`30000-32767`) with `kubectl get svc web-app-svc`.
2. Scale `web-app` to 1 replica and run `kubectl get endpoints web-app-svc` — watch the endpoint list shrink automatically.
3. Clean up:
   ```bash
   kubectl delete -f service.yaml
   kubectl delete -f ../02-deployments-and-scaling/deployment.yaml
   ```

---

Next: [Module 04 — ConfigMaps & Secrets](../04-configmaps-and-secrets/README.md)
