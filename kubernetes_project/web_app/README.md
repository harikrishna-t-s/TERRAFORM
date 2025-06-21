# Kubernetes Learning Web Application

A simple Flask web application designed for learning Docker and Kubernetes concepts. This application provides a foundation for understanding containerization, orchestration, and DevOps practices.

## 🚀 Features

- **Simple Web Interface**: Clean, responsive web UI with application information
- **Health Check Endpoint**: Kubernetes-ready health monitoring
- **API Endpoints**: RESTful API for testing and integration
- **Environment Configuration**: Configurable via environment variables
- **System Information**: Real-time system and application status
- **Docker Ready**: Optimized Dockerfile with multi-stage build
- **Kubernetes Compatible**: Designed for container orchestration

## 📋 Prerequisites

- Python 3.8 or higher
- Docker (for containerization)
- Kubernetes cluster (for orchestration)

## 🛠️ Local Development Setup

### 1. Clone and Navigate
```bash
cd kubernetes_project/web_app
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 🐳 Docker Usage

### Build the Docker Image
```bash
docker build -t kubernetes-learning-app .
```

### Run the Container
```bash
docker run -p 5000:5000 kubernetes-learning-app
```

### Run with Environment Variables
```bash
docker run -p 5000:5000 \
  -e ENVIRONMENT=production \
  -e APP_NAME="My Production App" \
  -e APP_VERSION="2.0.0" \
  kubernetes-learning-app
```

### Build for Different Architectures
```bash
# Build for multiple platforms
docker buildx build --platform linux/amd64,linux/arm64 -t kubernetes-learning-app .
```

## ☸️ Kubernetes Deployment

### 1. Create Namespace
```bash
kubectl create namespace learning-app
```

### 2. Apply Kubernetes Manifests
```bash
# Deploy the application
kubectl apply -f k8s/deployment.yaml

# Create service
kubectl apply -f k8s/service.yaml

# Create ingress (if using ingress controller)
kubectl apply -f k8s/ingress.yaml
```

### 3. Check Deployment Status
```bash
kubectl get pods -n learning-app
kubectl get services -n learning-app
kubectl get ingress -n learning-app
```

### 4. Access the Application
```bash
# Port forward to access locally
kubectl port-forward -n learning-app svc/learning-app-service 8080:80

# Or access via ingress (if configured)
curl http://your-ingress-domain
```

## 📡 API Endpoints

### Health Check
```bash
GET /health
```
Returns application health status for Kubernetes probes.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00",
  "app_name": "Kubernetes Learning App",
  "version": "1.0.0",
  "environment": "production"
}
```

### Application Info
```bash
GET /api/info
```
Returns detailed application and system information.

**Response:**
```json
{
  "application": {
    "name": "Kubernetes Learning App",
    "version": "1.0.0",
    "environment": "production"
  },
  "system": {
    "hostname": "pod-name",
    "platform": "Linux-5.4.0-x86_64",
    "python_version": "3.11.0",
    "environment": "production",
    "timestamp": "2024-01-01T12:00:00"
  },
  "request": {
    "method": "GET",
    "url": "http://localhost:5000/api/info",
    "headers": {...},
    "remote_addr": "127.0.0.1"
  }
}
```

### Echo Endpoint
```bash
POST /api/echo
Content-Type: application/json

{
  "message": "Hello World",
  "data": {"key": "value"}
}
```

**Response:**
```json
{
  "message": "Echo response",
  "received_data": {
    "message": "Hello World",
    "data": {"key": "value"}
  },
  "timestamp": "2024-01-01T12:00:00"
}
```

## 🔧 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `5000` | Port to run the application on |
| `HOST` | `0.0.0.0` | Host to bind the application to |
| `ENVIRONMENT` | `development` | Application environment |
| `APP_NAME` | `Kubernetes Learning App` | Application name |
| `APP_VERSION` | `1.0.0` | Application version |
| `SECRET_KEY` | `dev-secret-key-change-in-production` | Flask secret key |

## 📊 Monitoring and Health Checks

The application includes built-in health checks suitable for Kubernetes:

- **Liveness Probe**: `/health` endpoint
- **Readiness Probe**: `/health` endpoint
- **Health Check**: Docker HEALTHCHECK instruction

### Kubernetes Probe Configuration
```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 5000
  initialDelaySeconds: 30
  periodSeconds: 10
readinessProbe:
  httpGet:
    path: /health
    port: 5000
  initialDelaySeconds: 5
  periodSeconds: 5
```

## 🔍 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Check what's using the port
   lsof -i :5000
   # Kill the process or use a different port
   ```

2. **Docker Build Fails**
   ```bash
   # Clean Docker cache
   docker system prune -a
   # Rebuild without cache
   docker build --no-cache -t kubernetes-learning-app .
   ```

3. **Kubernetes Pod Not Starting**
   ```bash
   # Check pod logs
   kubectl logs -n learning-app <pod-name>
   # Check pod events
   kubectl describe pod -n learning-app <pod-name>
   ```

### Debug Mode
Set `ENVIRONMENT=development` to enable Flask debug mode for detailed error messages.

## 📚 Learning Path

This application is designed to help you learn:

1. **Docker Basics**
   - Containerization concepts
   - Dockerfile creation
   - Image building and optimization
   - Multi-stage builds

2. **Kubernetes Fundamentals**
   - Pod deployment
   - Service creation
   - Health checks and probes
   - Scaling and load balancing

3. **DevOps Practices**
   - CI/CD pipelines
   - Monitoring and logging
   - Environment management
   - Security best practices

## 🤝 Contributing

Feel free to enhance this application for your learning needs:

1. Add new API endpoints
2. Implement database integration
3. Add authentication
4. Create more complex deployment scenarios
5. Add monitoring and logging

## 📄 License

This project is for educational purposes. Feel free to use and modify as needed.

## 🔗 Useful Resources

- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Kubernetes Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/)

---

**Happy Learning! 🚀** 