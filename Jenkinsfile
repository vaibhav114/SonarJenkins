pipeline {
    agent any
    environment {
        SONAR_TOKEN = credentials('SONAR_TOKEN') // Store SonarCloud token in Jenkins credentials
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Add your build steps here
                sh './gradlew build' // Example for a Gradle build
            }
        }
        stage('SonarCloud Analysis') {
            steps {
                withSonarQubeEnv('SonarCloud') { // Match the name configured in Jenkins
                    sh '''
                        sonar-scanner \
                        -Dsonar.projectKey=your-project-key \
                        -Dsonar.organization=your-organization-key \
                        -Dsonar.host.url=https://sonarcloud.io \
                        -Dsonar.login=$SONAR_TOKEN
                    '''
                }
            }
        }
        stage('Quality Gate') {
            steps {
                script {
                    def qualityGate = waitForQualityGate()
                    if (qualityGate.status != 'OK') {
                        error "Pipeline failed due to SonarCloud Quality Gate: ${qualityGate.status}"
                    }
                }
            }
        }
    }
}
