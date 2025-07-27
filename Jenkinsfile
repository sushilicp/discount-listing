pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                cleanWs()
                git branch: 'main', url: 'https://github.com/sushilicp/discount-listing.git'
            }
        }
        stage('Build') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate.bat && pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                bat 'venv\\Scripts\\activate.bat && python manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                bat 'venv\\Scripts\\activate.bat && gunicorn --bind 0.0.0.0:8000 discount_listing.wsgi'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}