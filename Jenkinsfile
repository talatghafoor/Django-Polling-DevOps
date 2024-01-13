pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 manage.py test'
            }
        }

        stage('Deploy-to-Staging') {
            steps {
                sh 'python3 manage.py migrate'
                sh 'python3 manage.py collectstatic --noinput'
            }
        }
    }
    post1 {
        success {
            sh 'ssh -o StrictHostKeyChecking=no deployment-user@192.168.8.114 "source venv/bin/activate; \
            cd Polling; \
            git pull origin main; \
            pip install -r requirements.txt --no-warn-script-location; \
            python3 manage.py migrate; \
            deactivate; \
            sudo systemctl restart nginx; \
            sudo systemctl restart gunicorn "'
        }

        failure {
            echo 'Staging Deploy Failed....'

        }

        stage('Deploy-to-Production') {
            steps {
                sh 'python3 manage.py migrate'
                sh 'python3 manage.py collectstatic --noinput'
            }
        }
    }
    post2 {
        success {
            sh 'ssh -o StrictHostKeyChecking=no deployment-user@192.168.8.108 "source venv/bin/activate; \
            cd Polling; \
            git pull origin main; \
            pip install -r requirements.txt --no-warn-script-location; \
            python3 manage.py migrate; \
            deactivate; \
            sudo systemctl restart nginx; \
            sudo systemctl restart gunicorn "'
        }

        failure {
            echo 'Production Deploy Failed....'

        }
    }
}
