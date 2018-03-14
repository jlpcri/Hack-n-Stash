# KeystoneXXL Auto-Generated CI/CD Template

We've provided all the files you need to get started, but this is only half the story. Some of the things we used in the
hackathon to get to this point were already configured. We'd like to help you get the rest of the way there.

## Concourse to PCF

This is the best supported of our options as of today, as it deploys fully into PCF. However, you will need to have
Concourse access configured for you and an organization you can access in PCF.

manifest.yml is used to designate the content root of your project. The rest of the Concourse files are located in the
pipeline directory. ci/pipeline.yml and .concourse/keystoneXXL-properties.yml are the files you'll need to update with
the project and organization data for your project.

Please note that the Concourse server cannot access the internet to handle pip. Instead, you'll need to commit the files
to your repository. Keep requirements.txt up to date, and before deploying, run:

    mkdir vendor
    pip install --download vendor -r requirements.txt --no-binary :all:

You can read more about this at https://docs.cloudfoundry.org/buildpacks/python/index.html#vendoring

## Jenkins to Ansible Tower

As of this writing, this does not connect all the way into Ansible Tower. You will either need your AD account added to
the appropriate group or help from someone in the appropriate group to get your project deployed. Also, you will need a
Jenkins job created by a Jenkins administrator to monitor this repository.

Jenkinsfile is the relevant CI/CD file for this pipeline, but since the Ansible Tower configuration is not included,
you shouldn't have to alter anything in here for projects that don't require a discrete compilation step. Java, Kotlin,
.NET, et al. will need to edit in their build steps, but as you'll notice, we didn't offer these as target platforms!
The file as written will connect your repo to Jenkins (after job setup), Artifactory, and XRay.