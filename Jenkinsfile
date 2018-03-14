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
        def uploadSpec = """{
        "files": [
		  {
            "pattern": "hello.tar.gz",
            "target": "Hackathon/builds"
          }
		]
        }"""
        def buildInfo1 = server.upload(uploadSpec)
        server.publishBuildInfo(buildInfo1)
        def scanConfig = [
          'buildName'      : buildInfo1.name,
          'buildNumber'    : buildInfo1.number
        ]
        def scanResult = server.xrayScan scanConfig
        echo scanResult as String
      }
    }
    stage('scan') {
    }
  } finally {
    stage('cleanup') {
      echo "doing some cleanup..."
    }
  }
}
