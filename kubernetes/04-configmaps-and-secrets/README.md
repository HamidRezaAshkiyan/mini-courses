# Module 04: ConfigMaps & Secrets

## Why Externalize Configuration?

You want to build **one container image** and run it across dev, staging, and production without rebuilding it for every config change or baking passwords into the image.

- **ConfigMap**: Non-sensitive key-value data (feature flags, URLs, config files like `nginx.conf`).
- **Secret**: Sensitive data (API tokens, DB passwords, TLS certs). Stored base64-encoded in YAML (note: base64 is encoding, not encryption — in production, enable encryption-at-rest or use an external secrets manager).

Both can be injected into a Pod as **environment variables** or **mounted files**.

## Hands-On Lab

Run these commands from `kubernetes/04-configmaps-and-secrets`:

### 1. Apply the ConfigMap, Secret, and Pod

```bash
kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml
kubectl apply -f app-with-config.yaml
```

### 2. Verify environment variables and mounted files inside the container

```bash
kubectl exec config-demo -- env | grep -E "APP_|API_"
kubectl exec config-demo -- cat /etc/config/message.txt
```

You should see:
- `APP_ENV=development` (from ConfigMap)
- `API_KEY=super-secret-demo-token` (from Secret)
- The contents of `/etc/config/message.txt` (mounted as a file from ConfigMap)

## Try It Yourself

1. Edit `message.txt` inside [`configmap.yaml`](./configmap.yaml), re-apply it with `kubectl apply -f configmap.yaml`, wait ~30–60 seconds, and run `kubectl exec config-demo -- cat /etc/config/message.txt` again. Mounted ConfigMap files update automatically (whereas env vars require a Pod restart)!
2. Clean up:
   ```bash
   kubectl delete -f app-with-config.yaml -f secret.yaml -f configmap.yaml
   ```

---

Next: [Module 05 — Mini Project: 2-Tier App](../05-mini-project/README.md)
