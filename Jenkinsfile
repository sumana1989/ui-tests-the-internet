pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/YOUR_USERNAME/ui-tests-the-internet.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ui-tests:latest .'
            }
        }
        stage('Run Tests') {
            steps {
                docker.image('ui-tests:latest').inside {
                    sh 'python run_ui_test.py'
                }
            }
        }
    }
}
