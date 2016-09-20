from django.shortcuts import render

from .metadata import PROJECT_METADATA as PM


def start_view(request):
    if PM is not None:
        context = {"metadata": PM}
    else:
        context = {}

    return render(request, 'webpage/index.html', context)


def imprint_view(request):
    if PM is not None:
        context = {"metadata": PM}
    else:
        context = {}

    return render(request, 'webpage/imprint.html', context)
