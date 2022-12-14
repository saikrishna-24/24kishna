pipeline {
    agent any

    stages {
        stage('validate') {
            steps {
                echo 'validating code'
            }
        }
        stage('compile') {
            steps {
                echo 'compiling the code'
            }
        }
        stage('testing') {
            steps {
                echo 'testing the code'
            }
        }
        stage('deploy') {
            steps {
                echo 'deploying the code'
            }
        }
    }
}
