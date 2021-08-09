pipeline {
	agent any
	stages {
		stage('build') {
			steps {
				sh 'python3 --version'

				sh 'python3 -m venv .'
				sh 'chmod +x ./bin/activate'
				sh './bin/activate'

				sh './bin/pip3 install -r requirements.txt'
			}
		}
		stage('deploy') {
			steps {	
				sh './bin/python3 src/main.py &'
			}
		}
	}
}