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
                    sh 'wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.71/linux64/chrome-linux64.zip'
                    sh 'unzip chrome-linux64.zip'
                    sh 'sudo mv chrome-linux64 /usr/local/bin/'
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
