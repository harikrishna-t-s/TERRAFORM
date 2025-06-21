#!/bin/bash

# Development script for Kubernetes Learning Web Application
# This script provides common commands for development and testing

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to check if port is in use
port_in_use() {
    lsof -i :$1 >/dev/null 2>&1
}

# Function to setup virtual environment
setup_venv() {
    print_status "Setting up virtual environment..."
    if [ ! -d "venv" ]; then
        python3 -m venv venv
        print_success "Virtual environment created"
    else
        print_warning "Virtual environment already exists"
    fi
    
    source venv/bin/activate
    pip install -r requirements.txt
    print_success "Dependencies installed"
}

# Function to run the application locally
run_local() {
    print_status "Starting application locally..."
    if port_in_use 5000; then
        print_error "Port 5000 is already in use"
        print_status "You can kill the process or use a different port"
        exit 1
    fi
    
    source venv/bin/activate
    python app.py
}

# Function to test the application
test_app() {
    print_status "Testing application..."
    if ! command_exists python3; then
        print_error "Python3 is not installed"
        exit 1
    fi
    
    # Install requests if not available
    source venv/bin/activate
    pip install requests >/dev/null 2>&1 || true
    
    # Start app in background
    python app.py &
    APP_PID=$!
    
    # Wait for app to start
    sleep 3
    
    # Run tests
    python test_app.py
    TEST_RESULT=$?
    
    # Kill app
    kill $APP_PID 2>/dev/null || true
    
    if [ $TEST_RESULT -eq 0 ]; then
        print_success "All tests passed!"
    else
        print_error "Some tests failed"
        exit 1
    fi
}

# Function to build Docker image
build_docker() {
    print_status "Building Docker image..."
    if ! command_exists docker; then
        print_error "Docker is not installed"
        exit 1
    fi
    
    docker build -t kubernetes-learning-app .
    print_success "Docker image built successfully"
}

# Function to run Docker container
run_docker() {
    print_status "Running Docker container..."
    if ! command_exists docker; then
        print_error "Docker is not installed"
        exit 1
    fi
    
    if port_in_use 5000; then
        print_warning "Port 5000 is in use, using port 5001"
        PORT=5001
    else
        PORT=5000
    fi
    
    docker run -p $PORT:5000 kubernetes-learning-app &
    print_success "Docker container started on port $PORT"
    print_status "Access the application at http://localhost:$PORT"
}

# Function to clean up
cleanup() {
    print_status "Cleaning up..."
    
    # Kill any running containers
    docker stop $(docker ps -q --filter ancestor=kubernetes-learning-app) 2>/dev/null || true
    
    # Remove containers
    docker rm $(docker ps -aq --filter ancestor=kubernetes-learning-app) 2>/dev/null || true
    
    # Remove images
    docker rmi kubernetes-learning-app 2>/dev/null || true
    
    print_success "Cleanup completed"
}

# Function to show help
show_help() {
    echo "Kubernetes Learning Web Application - Development Script"
    echo ""
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  setup     - Setup virtual environment and install dependencies"
    echo "  run       - Run the application locally"
    echo "  test      - Test the application functionality"
    echo "  docker    - Build and run Docker container"
    echo "  build     - Build Docker image only"
    echo "  cleanup   - Clean up Docker containers and images"
    echo "  help      - Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 setup    # Setup development environment"
    echo "  $0 run      # Run application locally"
    echo "  $0 test     # Test application"
    echo "  $0 docker   # Build and run with Docker"
}

# Main script logic
case "${1:-help}" in
    setup)
        setup_venv
        ;;
    run)
        run_local
        ;;
    test)
        test_app
        ;;
    docker)
        build_docker
        run_docker
        ;;
    build)
        build_docker
        ;;
    cleanup)
        cleanup
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        print_error "Unknown command: $1"
        show_help
        exit 1
        ;;
esac 