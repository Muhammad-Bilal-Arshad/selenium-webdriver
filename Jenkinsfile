pipeline {
    agent any
    
    stages {
        stage('Remove Old Chromedriver') {
            steps {
                script {
                    sh 'sudo rm /usr/local/bin/chromedriver'
                }
            }
        }
        
        stage('Update Chromedriver') {
            steps {
                script {
                    sh 'wget https://chromedriver.storage.googleapis.com/120.0.6099.71/chromedriver_linux64.zip'
                    sh 'unzip chromedriver_linux64.zip'
                    sh 'sudo mv chromedriver /usr/local/bin/'
                }
            }
        }
        
        stage('Run Test') {
            steps {
                script {
                    sh 'python3 01-04-test-script.py'
                }
            }
        }
    }
}
