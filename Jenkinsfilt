pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sushilicp/discount-listing.git'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh '. venv/bin/activate && python manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                sh '. venv/bin/activate && gunicorn --bind 0.0.0.0:8000 discount_listing.wsgi'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}