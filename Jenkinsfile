pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-app"
        KUBE_NAMESPACE = "default"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${IMAGE_NAME}:latest .'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh '''
                    kubectl apply -f kubernetes/deployment.yaml
                    kubectl apply -f kubernetes/service.yaml
                    '''
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                script {
                    sh '''
                    kubectl rollout status deployment/flask-app
                    kubectl get pods
                    kubectl get services
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "Deployment to Kubernetes successful!"
        }
        failure {
            echo "Deployment failed!"
        }
    }
}
