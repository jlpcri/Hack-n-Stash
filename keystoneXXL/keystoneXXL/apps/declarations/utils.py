import os
import shutil
import subprocess

from django.conf import settings


def make_django_repo(repo_name, user, language, platform):
    subprocess.call(["git", "clone", "git@repo.sandbox.west.com:{0}/{1}.git".format(user, repo_name),
                     os.path.join(settings.TEMP_REPO_DIR, repo_name)])
    shutil.copytree(os.path.join(settings.BASE_DIR, "../repos/{0}/projname".format(language)),
                    os.path.join(settings.TEMP_REPO_DIR, repo_name, 'projname'))
    os.rename(os.path.join(settings.TEMP_REPO_DIR, repo_name, 'projname'),
              os.path.join(settings.TEMP_REPO_DIR, repo_name, repo_name))
    os.chdir(os.path.join(settings.TEMP_REPO_DIR, repo_name))
    subprocess.call(['git', 'add', '--all'])
    subprocess.call(['git', 'commit', '-m', '"First commit, courtesy of KeystoneXXL"'])
    subprocess.call(['git', 'push'])
