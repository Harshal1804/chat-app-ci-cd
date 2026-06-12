CI/CD Pipeline Automation using Jenkins, Docker & AWS EC2

A DevOps project demonstrating end-to-end CI/CD pipeline automation using Jenkins, Docker, and AWS EC2 with a sample chat application.

⸻

Project Overview

This project demonstrates how a CI/CD pipeline can automate the process of building, containerizing, and deploying an application to a staging server hosted on AWS EC2.

A sample chat application was used to simulate a real-world deployment workflow where Jenkins automatically handles:

* Source code integration
* Build automation
* Docker image creation
* Container deployment
* Continuous delivery to EC2 staging environment

⸻

Objectives

* Automate application deployment workflow
* Implement CI/CD using Jenkins
* Containerize application using Docker
* Deploy application on AWS EC2
* Reduce manual deployment effort
* Simulate real-world DevOps practices

⸻

Tech Stack

DevOps Tools

* Jenkins
* Docker
* Git & GitHub
* AWS EC2

Application

* Python / Flask Chat Application
* Linux Environment

⸻

CI/CD Workflow

The pipeline automates the following process:

1. Developer pushes code to GitHub
2. Jenkins detects repository changes
3. Jenkins pulls latest source code
4. Docker image is built automatically
5. Existing containers are stopped and removed
6. New container is deployed on EC2 staging server
7. Updated application becomes available automatically

⸻

Architecture Overview

Developer → GitHub → Jenkins Pipeline → Docker Build → EC2 Deployment

⸻

Features

* Automated build pipeline
* Dockerized application deployment
* Jenkins pipeline integration
* Continuous deployment on AWS EC2
* Reduced manual deployment steps
* Staging environment setup
* Container lifecycle automation

⸻

Project Structure

.
├── Jenkinsfile
├── Dockerfile
├── app/
├── requirements.txt
├── screenshots/
└── README.md

⸻

Jenkins Pipeline Stages

1. Source Code Checkout

Jenkins fetches latest code from GitHub repository.

2. Build Stage

Application dependencies and environment are prepared.

3. Docker Image Creation

Docker image is built automatically using Dockerfile.

4. Deployment Stage

Container is deployed on AWS EC2 staging server.

⸻

Dockerization

The application was containerized using Docker to ensure:

* Consistent runtime environment
* Easy deployment
* Scalability
* Isolation of dependencies

⸻

AWS EC2 Deployment

The staging server was hosted on AWS EC2 where Jenkins deployed the Docker container automatically after successful pipeline execution.

⸻

How to Run the Project

Clone Repository

git clone https://github.com/Prajwaldhawale/chat-app-ci-cd.git

Build Docker Image

docker build -t chat-app .

Run Docker Container

docker run -p 5000:5000 chat-app

⸻

Jenkins Setup

The project requires:

* Jenkins installed on EC2/local server
* Docker installed and configured
* GitHub repository integration
* Jenkins pipeline configuration
* Docker permissions for Jenkins user

⸻

Learning Outcomes

* Learned CI/CD pipeline automation
* Understood Jenkins pipeline workflow
* Practiced Docker containerization
* Worked with AWS EC2 deployment
* Learned staging server deployment process
* Improved DevOps automation understanding

⸻

Future Improvements

* Add Kubernetes deployment
* Implement GitHub Actions workflow
* Add monitoring with Prometheus & Grafana
* Configure Nginx reverse proxy
* Add SSL using HTTPS
* Implement rolling deployments
* Add automated testing stage

⸻

Screenshots

Add screenshots of:

<img width="1280" height="1076" alt="jenkins-running-on-aws" src="https://github.com/user-attachments/assets/4f75824d-083c-4ae4-a1c0-ffb8dc0090ee" />
<img width="1280" height="685" alt="Pipeline-executed" src="https://github.com/user-attachments/assets/6bfb3aac-2fcc-4b69-baf3-1aea4fd212b7" />
<img width="1280" height="768" alt="aws instance" src="https://github.com/user-attachments/assets/f5dcf87f-fc37-43e7-9cfd-d9213d59d095" />
<img width="864" height="424" alt="chat-app" src="https://github.com/user-attachments/assets/ec65dfdb-5f84-4c2d-b472-7c21a5521cc6" />
<img width="1467" height="918" alt="workflow" src="https://github.com/user-attachments/assets/53cc503f-203d-4617-9317-669a6b59dea8" />
<img width="2816" height="1536" alt="Architecture" src="https://github.com/user-attachments/assets/77f1c321-0fde-45b4-bb11-3bc6943ed1e8" />


⸻

Author

Prajwal Dhawale
