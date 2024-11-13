pipeline {
    agent any

    environment {
        PROJECT_DIR = '/home/jenkins/DevOps1909'
        VENV_DIR = "${PROJECT_DIR}/.venv"
    }

    stages {
        stage('Setup Python Environment') {
            steps {
                script {
                    // Check if Python virtual environment exists, if not, create it
                    if (!fileExists("${VENV_DIR}/bin/activate")) {
                        sh "python3 -m venv ${VENV_DIR}"
                    }
                }
                // Use bash to activate the virtual environment and install dependencies
                sh """
                    #!/bin/bash
                    source ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r ${PROJECT_DIR}/requirements.txt
                """
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Use bash to run your Python Selenium script
                sh """
                    #!/bin/bash
                    source ${VENV_DIR}/bin/activate
                    python ${PROJECT_DIR}/selenium_test.py
                """
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
