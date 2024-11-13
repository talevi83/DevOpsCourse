pipeline {
    agent any

    environment {
        VENV_DIR = '/home/jenkins/DevOps1909/.venv'
    }

    stages {
        stage('Clone Repository') {
            steps {
                dir('/home/jenkins/DevOps1909') {
                    git branch: 'main', url: 'https://github.com/talevi83/DevOpsCourse.git', credentialsId: 'github-token'
                }
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
                sh "${VENV_DIR}/bin/pip install -r /home/jenkins/DevOps1909/requirements.txt"
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh "${VENV_DIR}/bin/python /home/jenkins/DevOps1909/selenium_test.py"
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
