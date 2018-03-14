import os
import shutil
import subprocess

from django.conf import settings


def make_django_repo(repo_name, user, language, platform):
    # Clone repo
    subprocess.call(["git", "clone", "git@repo.sandbox.west.com:{0}/{1}.git".format(user, repo_name),
                     os.path.join(settings.TEMP_REPO_DIR, repo_name)])

    # Copy in repo directory
    shutil.copytree(os.path.join(settings.BASE_DIR, "../repos/{0}/projname".format(language)),
                    os.path.join(settings.TEMP_REPO_DIR, repo_name, 'projname'))
    os.rename(os.path.join(settings.TEMP_REPO_DIR, repo_name, 'projname'),
              os.path.join(settings.TEMP_REPO_DIR, repo_name, repo_name))
    os.chdir(os.path.join(settings.TEMP_REPO_DIR, repo_name))

    # Copy platform files
    if platform == 'PCF':
        shutil.copy2(os.path.join(settings.BASE_DIR, "../manifest.yml"),
                     os.path.join(settings.TEMP_REPO_DIR, repo_name, repo_name, 'projname', 'manifest.yml'))
        shutil.copytree(os.path.join(settings.BASE_DIR, "../../keystoneXXL-pipeline"),
                        os.path.join(settings.TEMP_REPO_DIR, repo_name, repo_name + '-pipeline'))
    elif platform == 'Ansible':
        shutil.copy2(os.path.join(settings.BASE_DIR, "../../Jenkinsfile"),
                     os.path.join(settings.TEMP_REPO_DIR, repo_name, repo_name, 'Jenkinsfile'))
        shutil.copy2(os.path.join(settings.BASE_DIR, "../../test_hello.sh"),
                     os.path.join(settings.TEMP_REPO_DIR, repo_name, repo_name, 'test_hello.sh'))

    # Commit and push
    subprocess.call(['git', 'add', '--all'])
    subprocess.call(['git', 'commit', '-m', '"First commit, courtesy of KeystoneXXL"'])
    subprocess.call(['git', 'push'])
