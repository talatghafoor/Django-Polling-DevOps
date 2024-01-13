// pipeline {
//     agent any
//     stages {
//         stage('Checkout') {
//             steps {
//                 checkout scm
//             }
//         }
//         stage('Install Dependencies') {
//             steps {
//                 sh 'pip install -r requirements.txt'
//             }
//         }

//         stage('Run Tests') {
//             steps {
//                 sh 'python3 manage.py test'
//             }
//         }

//         stage('Deploy') {
//             steps {
//                 sh 'python3 manage.py migrate'
//                 sh 'python3 manage.py collectstatic --noinput'
//             }
//         }
//     }
//     post {
//         success {
//             sh 'ssh -o StrictHostKeyChecking=no deployment-user@192.168.8.108 "source venv/bin/activate; \
//             cd Polling; \
//             git pull origin main; \
//             pip install -r requirements.txt --no-warn-script-location; \
//             python3 manage.py migrate; \
//             deactivate; \
//             sudo systemctl restart nginx; \
//             sudo systemctl restart gunicorn "'
//         }

//         failure {
//             echo 'Pipeline failed! Notify the team...'

//         }
//     }
// }

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

        stage('Deploy-to-Staging-Server') {
            steps {
                sh 'python3 manage.py migrate'
                sh 'python3 manage.py collectstatic --noinput'
                sh 'ssh -o StrictHostKeyChecking=no deployment-user@192.168.8.114 "source venv/bin/activate; \
                    cd Polling; \
                    git pull origin main; \
                    pip install -r requirements.txt --no-warn-script-location; \
                    python3 manage.py migrate; \
                    deactivate; \
                    sudo systemctl restart nginx; \
                    sudo systemctl restart gunicorn "'
            }
        }

        stage('Deploy-to-Production-Server') {
            steps {
                sh 'python3 manage.py migrate'
                sh 'python3 manage.py collectstatic --noinput'
                sh 'ssh -o StrictHostKeyChecking=no deployment-user@192.168.8.108 "source venv/bin/activate; \
                    cd Polling; \
                    git pull origin main; \
                    pip install -r requirements.txt --no-warn-script-location; \
                    python3 manage.py migrate; \
                    deactivate; \
                    sudo systemctl restart nginx; \
                    sudo systemctl restart gunicorn "'
            }
        }
    }
    post {
        success {
            echo 'Pipeline succeeded! Notify the team...'
        }

        failure {
            echo 'Pipeline failed! Notify the team...'
        }
    }
}

