# DevOps Project

Containerized Flask + MySQL application deployed on Kubernetes with Jenkins CI/CD and monitoring using Prometheus & Grafana.

---

## Tech Stack

* Flask
* MySQL
* Docker
* Kubernetes
* Jenkins
* Prometheus
* Grafana

---

## Features

* User Login & Registration
* Dockerized Application
* Jenkins CI/CD Pipeline
* Kubernetes Deployments & Services
* Kubernetes Secrets
* Pod CPU & Memory Monitoring
* Grafana Dashboard Visualization

---

---

## Monitoring

```promql id="slf2rw"
sum(rate(container_cpu_usage_seconds_total{pod=~".*flask.*",container!="POD"}[5m])) by (pod) * 100
```

---

## Author

Kathan Trivedi
