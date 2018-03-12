from django.shortcuts import render


def selections(request):
    if request.method == 'POST':
        raise NotImplementedError
    languages = ['Python', 'PHP']
    return render(request, 'selections.html', {'languages': languages})