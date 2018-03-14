from django.shortcuts import render, redirect

import requests

from keystoneXXL.apps.declarations.utils import make_django_repo


def selections(request):
    if request.method == 'POST':
        payload = {'name': request.POST['github'],
                   'description': 'Repository created via KeystoneXXL',
                   'homepage': 'http://{0}.app.pcfdev.one.west.com'.format(request.POST['github'])}
        r = requests.post("https://repo.sandbox.west.com/api/v3/user/repos",
                          auth=("caheyden", "e4f953b5feb8b89946bd917d166ae22ccc9978a1"), verify=False, json=payload)
        if r.status_code >= 400:
            raise RuntimeError("Repository creation failed - " + r.text)
        make_django_repo(repo_name=request.POST['github'],
                         user=request.POST['owner'],
                         platform=request.POST['platform'],
                         language=request.POST['language'])
        if request.POST['owner'] != 'caheyden':
            r = requests.post("https://repo.sandbox.west.com/api/v3/repos/caheyden/{0}/transfer".format(request.POST['github']),
                              auth=("caheyden", "e4f953b5feb8b89946bd917d166ae22ccc9978a1"), verify=False,
                              json={'new_owner': request.POST['owner']},
                              headers={'accept': 'application/vnd.github.nightshade-preview+json'})
            if r.status_code >= 400:
                raise RuntimeError("Repository transfer failed - " + r.text)
        return redirect("https://repo.sandbox.west.com/{0}/{1}".format(request.POST['owner'], request.POST['github']))

    languages = ['Python-Django', 'PHP']
    return render(request, 'selections.html', {'languages': languages})