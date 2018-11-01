stage("输出安装列表"){
  def userInput = input ( message : 'Select deployment versión and input deployment code:',
       parameters: [[$class: 'TextParameterDefinition', defaultValue: '', description: 'Clarive code', name: 'code']] )
}
