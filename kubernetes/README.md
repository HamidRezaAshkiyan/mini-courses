# Kubernetes Basics — Mini Course

Learn the core building blocks of Kubernetes (K8s) by deploying, scaling, exposing, and configuring real workloads on a local cluster.

## Prerequisites

- Basic familiarity with Docker / containers
- `kubectl` installed (`kubectl version --client`)
- A local Kubernetes cluster — any one of these works:
  - **Docker Desktop** → Settings → Kubernetes → Enable Kubernetes
  - **kind**: `brew install kind && kind create cluster`
  - **minikube**: `brew install minikube && minikube start`

Verify your cluster is ready:

```bash
kubectl cluster-info
kubectl get nodes
```

> No local cluster yet? You can spin up a free browser-based Kubernetes sandbox on [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes) and run every lab there.

## Syllabus

| # | Module | Core Concepts |
| --- | --- | --- |
| 01 | [Containers & Pods](./01-containers-and-pods/README.md) | What a Pod is, declarative YAML, `apply`, `logs`, `exec`, `describe` |
| 02 | [Deployments & Scaling](./02-deployments-and-scaling/README.md) | ReplicaSets, self-healing, scaling, rolling updates, rollbacks |
| 03 | [Services & Networking](./03-services-and-networking/README.md) | Labels/selectors, ClusterIP vs NodePort, internal DNS, port-forwarding |
| 04 | [ConfigMaps & Secrets](./04-configmaps-and-secrets/README.md) | External configuration, env vars, mounted config files, Secrets |
| 05 | [Mini Project: 2-Tier App](./05-mini-project/README.md) | Namespaces, connecting a web tier to Redis, debugging end-to-end |

## Quick `kubectl` Cheat Sheet

```bash
# Apply / delete manifests
kubectl apply -f file.yaml
kubectl delete -f file.yaml

# Inspect resources
kubectl get pods,deploy,svc
kubectl get pods -o wide
kubectl describe pod <name>

# Debug running containers
kubectl logs <pod-name>
kubectl logs -f <pod-name>
kubectl exec -it <pod-name> -- sh

# Access a Pod or Service from your laptop
kubectl port-forward svc/<service-name> 8080:80
```
