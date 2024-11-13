pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
    }

    stages {
        stage('Install Python3') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-venv python3-pip
                '''
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    if (!fileExists("${VENV_DIR}/bin/activate")) {
                        sh "python3 -m venv ${VENV_DIR}"
                    }
                }
                sh "${VENV_DIR}/bin/pip install --upgrade pip"
                sh "${VENV_DIR}/bin/pip install -r requirements.txt"
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh "${VENV_DIR}/bin/python your_selenium_script.py"
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
