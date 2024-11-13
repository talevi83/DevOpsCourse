pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
    }

    stages {
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
                sh "${VENV_DIR}/bin/python selenium_test.py"
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
