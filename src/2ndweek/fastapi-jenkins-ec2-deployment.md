# Simplified Deployment of FastAPI to AWS EC2 using Jenkins

This guide provides a streamlined process for deploying a FastAPI application with basic metrics to an AWS EC2 instance using Jenkins for CI/CD.

## Prerequisites

1. AWS account with necessary permissions
2. Jenkins server set up and running
3. Docker installed on the Jenkins server
4. AWS CLI installed and configured on the Jenkins server

## Step 1: Prepare the FastAPI Application

1. Create a directory for your project:
   ```bash
   mkdir fastapi-ec2-project
   cd fastapi-ec2-project
   ```

2. Create a `requirements.txt` file:
   ```
   fastapi
   uvicorn
   prometheus-client
   ```

3. Create a `main.py` file:
   ```python
   from fastapi import FastAPI
   from prometheus_client import Counter, generate_latest
   from prometheus_client.exposition import CONTENT_TYPE_LATEST

   app = FastAPI()

   # Create a metric to track requests
   REQUESTS = Counter('http_requests_total', 'Total HTTP Requests')

   @app.get("/")
   async def root():
       REQUESTS.inc()  # Increment the counter
       return {"message": "Hello World"}

   @app.get("/metrics")
   async def metrics():
       return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

   if __name__ == "__main__":
       import uvicorn
       uvicorn.run(app, host="0.0.0.0", port=8000)
   ```

4. Create a `Dockerfile`:
   ```Dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   COPY main.py .

   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

## Step 2: Set Up GitHub Repository

1. Create a new repository on GitHub.
2. Initialize git in your local project directory:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

## Step 3: Set Up AWS EC2 Instance

1. Launch an EC2 instance:
   - Use Amazon Linux 2 AMI
   - Choose an instance type (t2.micro for testing)
   - Configure security group to allow inbound traffic on port 22 (SSH) and 8000 (FastAPI)
   - Create or use an existing key pair for SSH access

2. Install Docker on the EC2 instance:
   ```bash
   sudo yum update -y
   sudo amazon-linux-extras install docker
   sudo service docker start
   sudo usermod -a -G docker ec2-user
   ```

## Step 4: Set Up Jenkins Pipeline

1. In Jenkins, create a new pipeline job.
2. In the job configuration, set up the pipeline to use your GitHub repository.
3. Create a `Jenkinsfile` in your project root:

```groovy
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'your-docker-hub-username/fastapi-app'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
        EC2_INSTANCE = 'ec2-user@your-ec2-instance-public-dns'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                        docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push("latest")
                    }
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    sshagent(credentials: ['ec2-ssh-key']) {
                        sh """
                            ssh -o StrictHostKeyChecking=no ${EC2_INSTANCE} '
                                docker pull ${DOCKER_IMAGE}:${DOCKER_TAG}
                                docker stop fastapi-app || true
                                docker rm fastapi-app || true
                                docker run -d --name fastapi-app -p 8000:8000 ${DOCKER_IMAGE}:${DOCKER_TAG}
                            '
                        """
                    }
                }
            }
        }
    }
}
```

## Step 5: Set Up Jenkins Credentials

1. Add your Docker Hub credentials to Jenkins (ID: 'docker-hub-credentials')
2. Add your EC2 instance SSH key to Jenkins (ID: 'ec2-ssh-key')

## Step 6: Run the Jenkins Pipeline

1. Commit and push your changes to GitHub:
   ```bash
   git add .
   git commit -m "Add Jenkinsfile and update application"
   git push
   ```

2. In Jenkins, run the pipeline for your project.

3. The pipeline will:
   - Check out your code
   - Build a Docker image
   - Push the Docker image to Docker Hub
   - Deploy the application to your EC2 instance

## Step 7: Verify the Deployment

1. Access your FastAPI application using the EC2 instance's public DNS:
   ```
   http://<EC2-Public-DNS>:8000
   ```

2. Check the metrics endpoint:
   ```
   http://<EC2-Public-DNS>:8000/metrics
   ```

This completes the simplified deployment process. Your FastAPI application is now deployed on an AWS EC2 instance with basic metrics enabled, and you have a CI/CD pipeline set up with Jenkins for automated deployments.

