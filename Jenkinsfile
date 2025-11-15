pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'develop', url: 'https://github.com/i220493/flask-k8s-ci-cd-assignment.git'
            }
        }

        stage('Build Docker image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Run container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name flask-app-container flask-app'
            }
        }
    }
}
