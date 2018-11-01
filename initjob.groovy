#!groovy
pipeline {
    agent any
    parameters {
        text(name:'installlist', defaultValue: 'nginx', description: 'install list')
        string(name:'username', defaultValue: 'nginx', description: 'User name')
        password(name:'password', defaultValue: 'nginx', description: 'password')
    }
    stages{
        stage("Component L"){
            steps{
                  script{
                      echo "${params.installlist}"
                      installlist = "${params.installlist}"
                      sh 'python createplaybook.py -i $installlist'
                      // user = input ( message : 'Select deployment versión and input deployment code:', parameters: [[$class: 'TextParameterDefinition', defaultValue: '', description: 'Clarive code', name: 'code']] )
                  }
              }
        }

    }
}
