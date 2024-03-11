pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'
            }
        }
        stage('Deploy') {
            when {
                expression { return env.BRANCH_NAME == 'main' }
            }
            steps {
                script {
                    echo 'Deploying to production'
                }
            }
        }
    }
}
