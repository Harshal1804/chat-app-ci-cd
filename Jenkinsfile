pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t chat-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker rm -f chat-container || true'
                sh 'docker run -d -p 5001:5001 --name chat-container chat-app'
            }
        }

    }
}