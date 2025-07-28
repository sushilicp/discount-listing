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
                withCredentials([usernamePassword(credentialsId: 'pythonanywhere-api-cred', usernameVariable: 'PA_USERNAME', passwordVariable: 'PA_API_TOKEN')]) {
                    bat """
                    curl -X POST -u %PA_USERNAME%:%PA_API_TOKEN% ^
                    https://www.pythonanywhere.com/api/v0/user/%PA_USERNAME%/webapps/%PA_USERNAME%.pythonanywhere.com/reload/
                    """
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}