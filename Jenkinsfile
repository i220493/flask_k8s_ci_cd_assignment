pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t flask-app:latest .'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    bat 'kubectl apply -f k8s/deployment.yaml'
                    bat 'kubectl apply -f k8s/service.yaml'
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                script {
                    bat 'kubectl rollout status deployment/flask-deployment'
                    bat 'kubectl get pods'
                    bat 'kubectl get services'
                }
            }
        }
    }
}
