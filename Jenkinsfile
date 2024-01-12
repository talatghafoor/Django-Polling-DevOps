pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your version control system (e.g., Git)
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python and required dependencies
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run Django tests
                sh 'python3 manage.py test'
            }
        }

        stage('Deploy') {
            steps {
                // Your deployment steps go here
                // This can include migrating the database, collecting static files, etc.
                sh 'python3 manage.py migrate'
                sh 'python3 manage.py collectstatic --noinput'
                // Additional deployment steps as needed
            }
        }
    }

    post {
        success {
            // This block will be executed if the pipeline is successful
            sh 'ssh deployment-user@192.168.8.108 "source venv/bin/activate; \
            cd Polling; \
            git pull origin main; \
            pip install -r requirements.txt --no-warn-script-location; \
            python3 manage.py migrate; \
            deactivate; \
            sudo systemctl restart nginx; \
            sudo systemctl restart gunicorn "'
            // You may trigger a deployment to a staging or production environment here
        }

        failure {
            // This block will be executed if the pipeline fails
            echo 'Pipeline failed! Notify the team...'

        }
    }
}
