node {
  try {
    stage('checkout') {
      checkout scm
    }
    stage('prepare') {
      sh "git clean -fdx"
    }
    stage('compile') {
      echo "nothing to compile for hello.sh..."
    }
    stage('test') {
      sh "./test_hello.sh"
    }
    stage('package') {
      sh "tar -cvzf hello.tar.gz hello.sh"
    }
    stage('publish') {
      echo "uploading package..."
        steps {
          script {   
            def buildInfo
            def server = Artifactory.server ('artifacts')
            def uploadSpec = """{
            "files": [ {
            "pattern": "Jenkinsfile",
		    "target": "Hack-n-Stash/builds/" } ]
          }"""
    }
  } finally {
    stage('cleanup') {
      echo "doing some cleanup..."
    }
  }
}