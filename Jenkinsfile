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
<<<<<<< HEAD
      echo "uploading package..."
      script {
        def buildInfo
        def server = Artifactory.server ('artifacts')
        def uploadSpec = """{
        "files": [ {
        "pattern": "Jenkinsfile",
        "target": "Hack-n-Stash/builds/" } ]
        }"""
=======
      echo "uploading Package..."
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
        }
>>>>>>> ee69d1e6d5aaa4ef4b644f1d6966d65b3342755e
      }
    }
  } finally {
    stage('cleanup') {
      echo "doing some cleanup..."
    }
  }
}
