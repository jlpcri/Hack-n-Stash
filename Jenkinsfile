node {
  try {
    stage('checkout') {
      checkout scm
    }
    stage('prepare') {
      sh "git clean -fdx"
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
        buildInfo.retention maxBuilds: 10
        server.publishBuildInfo buildInfo
        def uploadSpec = """{
        "files": [
		  {
            "pattern": "hello.tar.gz",
            "target": "Hackathon/builds"
          }
		]
        }"""
        def buildInfo1 = server.upload(uploadSpec)
      }
    }
  } finally {
    stage('cleanup') {
      echo "doing some cleanup..."
    }
  }
}
