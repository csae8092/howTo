from django.shortcuts import render
from django.http import JsonResponse
from .metadata import PROJECT_METADATA as PM
from copy import deepcopy


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


#################################################################
#                    project info view                          #
#################################################################


def project_info(request):

    """
    returns a dict providing metadata about the current project
    """

    info_dict = deepcopy(PM)
    if request.user.is_anonymous:
        del info_dict['matomo_id']
        del info_dict['matomo_url']
    else:
        pass    
    info_dict['base_tech'] = 'django'
    info_dict['framework'] = 'djangobaseproject'
    return JsonResponse(info_dict)