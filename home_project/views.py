from django.views import generic
from django.shortcuts import render
import logging
import os

from . import SETUP_DATA


def about_view(request):
    """ View for showing the About form of the project """

    logging.info(f'{os.getenv("ID_LOG", "")} Showing the About form')

    template_name = 'home_project/about.html'

    return render(request, template_name, {'about_data': SETUP_DATA})



