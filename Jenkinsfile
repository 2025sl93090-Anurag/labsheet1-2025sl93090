pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code checked out successfully.'
            }
        }

        stage('Build') {
            steps {
                echo 'Build stage...'
                sh 'python3 --version'
                sh 'echo "Files in workspace:"'
                sh 'ls -la'
            }
        }

        stage('Test') {
            steps {
                echo ' Running tests...'
                sh 'python3 test_calculator.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy stage...'
                sh '''
                    mkdir -p /tmp/jenkins-deploy
                    cp calculator.py /tmp/jenkins-deploy/calculator.py
                    echo "Deployed files:"
                    ls -la /tmp/jenkins-deploy/
                    echo "Deployment to /tmp/jenkins-deploy successful!"
                '''
            }
        }

    }
}
