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
                git url: 'https://github.com/i220493/flask_k8s_ci_cd_assignment', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Use host's Docker
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Apply deployment and service
                    sh "kubectl apply -f ${DEPLOYMENT_FILE}"
                    sh "kubectl apply -f ${SERVICE_FILE}"
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                script {
                    sh "kubectl rollout status deployment/flask-deployment"
                    sh "kubectl get pods"
                    sh "kubectl get svc flask-service"
                }
            }
        }
    }
}
