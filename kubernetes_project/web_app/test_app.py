#!/usr/bin/env python3
"""
Test script for the Kubernetes Learning Web Application
=======================================================

This script tests the basic functionality of the Flask application
to ensure it's working correctly before containerization.
"""

import requests
import json
import time
import sys

def test_health_endpoint(base_url):
    """Test the health check endpoint."""
    print("Testing health endpoint...")
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check passed: {data['status']}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

def test_api_info_endpoint(base_url):
    """Test the API info endpoint."""
    print("Testing API info endpoint...")
    try:
        response = requests.get(f"{base_url}/api/info", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API info: {data['application']['name']} v{data['application']['version']}")
            return True
        else:
            print(f"❌ API info failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ API info error: {e}")
        return False

def test_echo_endpoint(base_url):
    """Test the echo endpoint."""
    print("Testing echo endpoint...")
    try:
        test_data = {"message": "Hello from test script", "timestamp": time.time()}
        response = requests.post(f"{base_url}/api/echo", 
                               json=test_data, 
                               timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data['received_data'] == test_data:
                print("✅ Echo endpoint working correctly")
                return True
            else:
                print("❌ Echo endpoint returned unexpected data")
                return False
        else:
            print(f"❌ Echo endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Echo endpoint error: {e}")
        return False

def test_main_page(base_url):
    """Test the main page."""
    print("Testing main page...")
    try:
        response = requests.get(base_url, timeout=5)
        if response.status_code == 200:
            print("✅ Main page accessible")
            return True
        else:
            print(f"❌ Main page failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Main page error: {e}")
        return False

def main():
    """Main test function."""
    base_url = "http://localhost:5000"
    
    print("🚀 Testing Kubernetes Learning Web Application")
    print("=" * 50)
    
    # Wait a moment for the app to start
    print("Waiting for application to start...")
    time.sleep(2)
    
    tests = [
        test_main_page,
        test_health_endpoint,
        test_api_info_endpoint,
        test_echo_endpoint
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test(base_url):
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Application is ready for Docker/Kubernetes deployment.")
        return 0
    else:
        print("❌ Some tests failed. Please check the application.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 