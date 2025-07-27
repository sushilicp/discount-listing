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
            script {
                def api_token = '4937b429de5a703d5226bc891ff2fb3409685577'
                def username = 'sushilicp'
                bat """
                curl -X POST --user ${username}:${api_token} ^
                https://www.pythonanywhere.com/api/v0/user/${username}/webapps/${username}.pythonanywhere.com/reload/
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