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
	    script {
        def buildInfo
        def server = Artifactory.server ('artifacts')
        def uploadSpec = """{
        "files": [
		  {
            "pattern": "hello*",
            "target": "Hack-n-Stash/builds/"
          }
		]
        }"""
		server.upload(uploadSpec)
      }
    }
  } finally {
    stage('cleanup') {
      echo "doing some cleanup..."
    }
  }
}
