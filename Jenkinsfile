pipeline {
    stages {
        stage('SCM checkout') {
            git url: 'https://github.com/noracamillaa/python_test', branch: 'main'

            echo "Git SCM chekout"
        }
    }
}

pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}


// working
pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('SCM checkout') {
            steps{
                git url: 'https://github.com/noracamillaa/python_test', branch: 'main'
    
                echo "Git SCM chekout"
            }
        }
    }
}