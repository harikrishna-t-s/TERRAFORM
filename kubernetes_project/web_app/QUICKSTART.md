# Quick Start Guide

This guide will help you get the Kubernetes Learning Web Application running quickly for your learning journey.

## 🚀 Quick Start (5 minutes)

### 1. Setup Development Environment
```bash
cd kubernetes_project/web_app
./dev.sh setup
```

### 2. Test the Application Locally
```bash
./dev.sh test
```

### 3. Run the Application
```bash
./dev.sh run
```

Visit `http://localhost:5000` to see your application!

## 🐳 Docker Quick Start

### 1. Build and Run with Docker
```bash
./dev.sh docker
```

### 2. Or manually:
```bash
# Build image
docker build -t kubernetes-learning-app .

# Run container
docker run -p 5000:5000 kubernetes-learning-app
```

## ☸️ Kubernetes Quick Start

### Prerequisites
- Kubernetes cluster (Minikube, Docker Desktop, or cloud cluster)
- kubectl configured

### 1. Build and Load Docker Image
```bash
# Build image
docker build -t kubernetes-learning-app .

# If using Minikube
minikube image load kubernetes-learning-app

# If using Docker Desktop
# Image is already available
```

### 2. Deploy to Kubernetes
```bash
# Apply all manifests
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/ingress.yaml

# Check deployment
kubectl get pods -n learning-app
kubectl get services -n learning-app
```

### 3. Access the Application
```bash
# Port forward to access locally
kubectl port-forward -n learning-app svc/kubernetes-learning-app-service 8080:80

# Visit http://localhost:8080
```

## 📋 What You'll Learn

### Phase 1: Application Basics
- [x] Simple Flask web application
- [x] Health check endpoints
- [x] Environment configuration
- [x] API testing

### Phase 2: Containerization
- [ ] Docker image building
- [ ] Multi-stage builds
- [ ] Container security
- [ ] Image optimization

### Phase 3: Kubernetes Deployment
- [ ] Pod deployment
- [ ] Service creation
- [ ] Health checks and probes
- [ ] Resource management

### Phase 4: Advanced Topics
- [ ] Scaling and load balancing
- [ ] Ingress configuration
- [ ] Monitoring and logging
- [ ] CI/CD integration

## 🔧 Common Commands

### Development
```bash
./dev.sh setup      # Setup environment
./dev.sh run        # Run locally
./dev.sh test       # Test application
./dev.sh docker     # Build and run with Docker
./dev.sh cleanup    # Clean up Docker resources
```

### Kubernetes
```bash
kubectl apply -f k8s/deployment.yaml    # Deploy application
kubectl get pods -n learning-app        # Check pods
kubectl logs -n learning-app <pod-name> # View logs
kubectl delete -f k8s/deployment.yaml   # Remove deployment
```

### Docker
```bash
docker build -t kubernetes-learning-app .           # Build image
docker run -p 5000:5000 kubernetes-learning-app     # Run container
docker ps                                          # List containers
docker stop <container-id>                         # Stop container
```

## 🎯 Next Steps

1. **Explore the Application**: Visit all endpoints and understand the functionality
2. **Modify the Code**: Add new features or endpoints
3. **Experiment with Docker**: Try different Docker configurations
4. **Deploy to Kubernetes**: Practice with different deployment strategies
5. **Add Monitoring**: Integrate logging and monitoring solutions

## 🆘 Need Help?

- Check the main [README.md](README.md) for detailed documentation
- Review the application code in `app.py`
- Test individual endpoints using the test script
- Use `./dev.sh help` for available commands

---

**Happy Learning! 🚀** 