from django.shortcuts import render

import requests


def selections(request):
    if request.method == 'POST':
        print(request.POST['language'])
        print(request.POST['github'])
        print(request.POST['owner'])
        print(request.POST['platform'])
        payload = {'name': request.POST['github'],
                   'description': 'Repository created via KeystoneXXL',
                   'homepage': 'http://{0}.app.pcfdev.one.west.com'.format(request.POST['github'])}
        r = requests.post("https://repo.sandbox.west.com/api/v3/user/repos",
                          auth=("caheyden", "e4f953b5feb8b89946bd917d166ae22ccc9978a1"), verify=False, json=payload)
        if r.status_code >= 400:
            raise RuntimeError("Repository creation failed - " + r.text)
        r = requests.post("https://repo.sandbox.west.com/api/v3/repos/caheyden/{0}/transfer".format(request.POST['github']),
                          auth=("caheyden", "e4f953b5feb8b89946bd917d166ae22ccc9978a1"), verify=False,
                          json={'new_owner': request.POST['owner']},
                          headers={'accept': 'application/vnd.github.nightshade-preview+json'})
        if r.status_code >= 400:
            raise RuntimeError("Repository transfer failed - " + r.text)

    languages = ['Python', 'PHP']
    return render(request, 'selections.html', {'languages': languages})