stages {

    stage('Checkout Code') {
        steps {
            checkout scm
        }
    }

    stage('Code Validation') {
        steps {
            sh 'python3 -m py_compile app.py'
        }
    }

    stage('Build Docker Image') {
        steps {
            sh 'docker build -t chat-app .'
        }
    }

    stage('Deploy Container') {
        steps {
            sh 'docker rm -f chat-container || true'
            sh 'docker run -d -p 5001:5001 --name chat-container chat-app'
        }
    }

    stage('Health Check') {
        steps {
            sh '''
                sleep 10
                curl -f http://localhost:5001 || exit 1
            '''
        }
    }
}

post {
    success {
        echo 'Pipeline executed successfully!'
    }

    failure {
        echo 'Pipeline failed!'
    }
}