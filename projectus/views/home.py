from django.shortcuts import render

from core import settings


def home(request):

    context ={ 
        'tag_title': f'{settings.SITENAME}'
    }
    return render(
        request,
        'projectus/home.html',
       context 
    )
