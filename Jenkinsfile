pipeline{
agent any
stages{
  stage('Checkout'){
    steps{
    git 'https://github.com/Nagashreer6515/PythonSelenium.git'
}
}
  stage('Build'){
   steps{
    bat 'python MyTest.py'
}
}
stage('HTML Report'){
  steps{
    publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: 'C:\\Users\\nagashreer\\PycharmProjects\\PythonProject2', reportFiles: 'index.html', reportName: 'HTML Report', reportTitles: '', useWrapperFileDirectly: true])
}
}
  stage('Finishing')
{
  steps{
  echo 'Build is completed..'
}
}
}
}
