CI/CD Pipeline Automation using Jenkins, Docker & AWS EC2

A complete DevOps implementation demonstrating Continuous Integration and Continuous Deployment (CI/CD) automation using Jenkins, Docker, GitHub Webhooks, and AWS EC2.

⸻

Project Overview

This project demonstrates an end-to-end CI/CD pipeline that automatically builds, validates, containerizes, and deploys a web application whenever code is pushed to GitHub.

The implementation simulates a real-world DevOps workflow by integrating GitHub, Jenkins, Docker, and AWS EC2 to eliminate manual deployment steps and ensure faster, more reliable software delivery.

⸻

Objectives

* Automate application deployment workflow
* Implement Continuous Integration using Jenkins
* Implement Continuous Deployment on AWS EC2
* Containerize applications using Docker
* Validate source code before deployment
* Automate container lifecycle management
* Reduce manual deployment effort
* Simulate industry-standard DevOps practices

⸻

Technology Stack

DevOps Tools

* Jenkins
* Docker
* Git
* GitHub
* GitHub Webhooks
* AWS EC2

Application Stack

* Python
* Flask
* SQLite Database
* HTML
* CSS
* JavaScript
* Linux (Ubuntu)

⸻

CI/CD Workflow

1. Developer pushes code to GitHub
2. GitHub Webhook triggers Jenkins automatically
3. Jenkins pulls the latest source code
4. Python source code validation is executed
5. Docker image is built automatically
6. Existing container is removed
7. New container is deployed
8. Health check validates deployment
9. Updated application becomes available to users

⸻

Architecture Overview

Developer → GitHub → GitHub Webhook → Jenkins Pipeline → Docker Build → Docker Container → AWS EC2 → End User

⸻

Key Features

* Real-time Chat Interface
* SQLite Database Integration
* Automated GitHub Webhook Trigger
* Continuous Integration Pipeline
* Source Code Validation
* Dockerized Application Deployment
* Automated Container Replacement
* Health Check Verification
* Continuous Deployment on AWS EC2
* Jenkins Pipeline as Code
* Reduced Manual Operations

⸻

Project Structure

chat-app-ci-cd/
│
├── screenshots/          # Project screenshots
├── static/               # CSS, JS and static assets
├── templates/            # HTML templates
│
├── app.py                # Main Flask application
├── database.db           # SQLite database
├── Dockerfile            # Docker image definition
├── Jenkinsfile           # CI/CD pipeline configuration
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

⸻

Jenkins Pipeline Stages

1. Checkout Code

Jenkins retrieves the latest source code from GitHub repository.

2. Code Validation

Python source code is validated before deployment.

python3 -m py_compile app.py

3. Build Docker Image

A fresh Docker image is created using Docker.

docker build -t chat-app .

4. Deploy Container

The previous container is removed and a new container is deployed.

docker rm -f chat-container || true
docker run -d -p 5001:5001 --name chat-container chat-app

5. Health Check

Deployment is verified automatically.

curl -f http://localhost:5001

⸻

Dockerization

Docker was used to provide:

* Consistent runtime environment
* Dependency isolation
* Simplified deployment
* Application portability
* Faster deployment and recovery

⸻

AWS EC2 Deployment

The application is hosted on an AWS EC2 Ubuntu instance.

The EC2 server hosts:

* Jenkins Server
* Docker Engine
* Chat Application Container

All deployment operations are executed automatically through Jenkins.

⸻

How to Run the Project

Clone Repository

git clone https://github.com/Prajwaldhawale/chat-app-ci-cd.git
cd chat-app-ci-cd

Build Docker Image

docker build -t chat-app .

Run Docker Container

docker run -d -p 5001:5001 --name chat-container chat-app

Access Application

http://localhost:5001

⸻

Jenkins Configuration Requirements

* Jenkins Installed
* Docker Installed
* Git Installed
* GitHub Repository Integration
* GitHub Webhook Configuration
* Docker Permissions for Jenkins User
* Port 8080 Open for Jenkins
* Port 5001 Open for Application Access

⸻

Learning Outcomes

* CI/CD Pipeline Automation
* Jenkins Pipeline Development
* Docker Containerization
* GitHub Webhook Integration
* AWS EC2 Deployment
* Automated Application Delivery
* Health Check Automation
* DevOps Workflow Implementation

⸻

Future Enhancements

* Automated Unit Testing Stage
* Docker Hub Integration
* Kubernetes Deployment
* Blue-Green Deployment Strategy
* Nginx Reverse Proxy
* HTTPS/SSL Configuration
* Monitoring with Prometheus
* Grafana Dashboard
* Infrastructure as Code using Terraform
* Multi-Environment Deployment

Author

Prajwal Dhawale

B.Tech Computer Science Engineering (Cloud Computing)