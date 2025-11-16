pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "flask-app:latest"
        DEPLOYMENT_FILE = "k8s/deployment.yaml"
        SERVICE_FILE = "k8s/service.yaml"
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
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }
        stage('Load Image to Minikube') {
            steps {
                script {
                    // Save image and load into minikube
                    sh "docker save ${DOCKER_IMAGE} | docker exec -i minikube docker load"
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh "kubectl apply -f ${DEPLOYMENT_FILE}"
                    sh "kubectl apply -f ${SERVICE_FILE}"
                }
            }
        }
        stage('Verify Deployment') {
            steps {
                script {
                    sh "kubectl rollout status deployment/flask-deployment --timeout=5m"
                    sh "kubectl get pods -l app=flask-app"
                    sh "kubectl get svc flask-service"
                }
            }
        }
    }
}
