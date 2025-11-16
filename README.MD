# Flask Kubernetes CI/CD Assignment

## Project Description

This project demonstrates a complete CI/CD pipeline for a Python Flask application deployed on Kubernetes. The pipeline integrates GitHub Actions for continuous integration, Jenkins for continuous delivery, and Kubernetes (minikube) for container orchestration.

### Kubernetes Features Used

- **Deployments**: Manages application replicas with rolling update strategy
- **Services**: Provides load balancing across pods using NodePort
- **Rolling Updates**: Zero-downtime deployments with configurable maxSurge and maxUnavailable
- **Scaling**: Dynamic pod scaling based on demand
- **Rollback**: Ability to revert to previous deployment versions
- **Resource Management**: CPU and memory limits/requests for optimal resource utilization

## Architecture
```
Developer Push → GitHub → GitHub Actions (CI) → Jenkins (CD) → Kubernetes (minikube)
                    ↓                              ↓                    ↓
                Lint/Test                    Build Docker         Deploy & Scale
                                             Load to minikube
```

## Prerequisites

- Docker Desktop
- Minikube
- kubectl
- Jenkins
- Python 3.10+

## How to Build and Run Locally with Docker

### 1. Build the Docker Image
```bash
docker build -t flask-app:latest .
```

### 2. Run the Container
```bash
docker run -p 5000:5000 flask-app:latest
```

### 3. Access the Application

Open your browser and navigate to:
```
http://localhost:5000
```

## How to Deploy to Kubernetes using Jenkins Pipeline

### 1. Start Minikube
```bash
minikube start
```

### 2. Configure Jenkins

- Install Jenkins with Docker and kubectl
- Configure kubectl to connect to minikube cluster
- Set up Jenkins pipeline job pointing to this repository

### 3. Jenkins Pipeline Stages

The Jenkinsfile defines the following stages:

1. **Checkout**: Clone the repository
2. **Build Docker Image**: Build the Flask application image
3. **Load Image to Minikube**: Transfer image to minikube's Docker daemon
4. **Deploy to Kubernetes**: Apply Kubernetes manifests
5. **Verify Deployment**: Check rollout status and pod health

### 4. Trigger Deployment

- Push code changes to GitHub
- Jenkins automatically triggers the pipeline
- Application deploys to Kubernetes cluster

### 5. Verify Deployment
```bash
kubectl get pods
kubectl get services
kubectl get deployments
```

## Kubernetes Features Explained

### Automated Rollouts

The deployment uses a **RollingUpdate** strategy:
```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxSurge: 1          # Maximum pods created above desired count
    maxUnavailable: 0    # Minimum pods available during update
```

**Benefits**:
- Zero downtime during updates
- Gradual rollout of new versions
- Automatic rollback on failure

**How it works**:
1. New pods are created one at a time
2. Once new pod is ready, old pod is terminated
3. Process repeats until all pods are updated

### Scaling

The deployment supports horizontal scaling:
```bash
# Scale up to 5 replicas
kubectl scale deployment flask-deployment --replicas=5

# Scale down to 2 replicas
kubectl scale deployment flask-deployment --replicas=2
```

**Benefits**:
- Handle increased traffic load
- High availability
- Load distribution across multiple pods

### Load Balancing

The Service resource provides load balancing:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: flask-service
spec:
  type: NodePort
  selector:
    app: flask-app
  ports:
    - port: 5000
      targetPort: 5000
      nodePort: 30007
```

**How it works**:
- Service distributes incoming traffic across all healthy pods
- Automatic service discovery within cluster
- External access via NodePort (30007)

**Access the application**:
```bash
# Get minikube IP
minikube ip

# Access application
http://<minikube-ip>:30007
```

### Rollback

If a deployment fails, easily rollback:
```bash
# View rollout history
kubectl rollout history deployment/flask-deployment

# Rollback to previous version
kubectl rollout undo deployment/flask-deployment

# Rollback to specific revision
kubectl rollout undo deployment/flask-deployment --to-revision=2
```

## CI/CD Pipeline Details

### GitHub Actions (CI)

Automatically runs on every push:
- ✅ Python environment setup
- ✅ Dependency installation
- ✅ Code linting (flake8, max line length: 90)
- ✅ Unit tests (pytest)
- ✅ Docker image build

### Jenkins (CD)

Triggered on merge to main:
- ✅ Build Docker image
- ✅ Load image to minikube
- ✅ Deploy to Kubernetes
- ✅ Verify deployment health

## Monitoring and Troubleshooting

### Check Pod Status
```bash
kubectl get pods -w
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

### Check Deployment Status
```bash
kubectl rollout status deployment/flask-deployment
kubectl get deployments
```

### Check Service
```bash
kubectl get services
kubectl describe service flask-service
```

### Common Issues

1. **ImagePullBackOff**: Ensure `imagePullPolicy: Never` is set in deployment.yaml
2. **Pods not starting**: Check `kubectl describe pod` for errors
3. **Service not accessible**: Verify NodePort and minikube IP

## Team Members

- **Sameer Asif (i220493)**: Repository setup, CI/CD implementation, Kubernetes configuration

## Technologies Used

- **Version Control**: Git, GitHub
- **CI**: GitHub Actions
- **CD**: Jenkins
- **Containerization**: Docker
- **Orchestration**: Kubernetes (minikube)
- **Programming**: Python, Flask
- **Tools**: kubectl, Docker CLI

## License

This project is for educational purposes as part of a CI/CD assignment.
