# by Richi Rod AKA @richionline / falken20

import logging
import os
from django.shortcuts import render, redirect

# When import login and logout we change the name (do_...) to avoid mistakes with methods names
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def welcome(request):
    """ Method to welcome the user """
    # The user login is ok
    if request.user.is_authenticated:
        return render(request, "users/welcome.html")

    # In other case
    return redirect('/login')


def logout(request):
    """ Method to end the user session """
    # End the session
    do_logout(request)

    # Redirect to home
    return redirect('/login')


def login(request):
    """ Method to login the user """
    # Create the authentication form empty
    form = AuthenticationForm()
    if request.method == "POST":
        # Set the data from request
        form = AuthenticationForm(data=request.POST)
        logging.info(f'{os.getenv("ID_LOG", "")} Form errors: {form.errors}')
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verify credentials
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                logging.info(f'{os.getenv("ID_LOG", "")} User login: {user}')
                return redirect('/welcome')

    return render(request, "users/login.html", {'form': form})


def register(request):
    """ Method to register the user """
    logging.info(f'{os.getenv("ID_LOG", "")} Starting to add a new user')

    # Create the authentication form empty
    form = UserCreationForm()
    # Hide the help text of the fields
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    if request.method == "POST":
        # Set the data from request
        form = UserCreationForm(data=request.POST)
        logging.info(f'{os.getenv("ID_LOG", "")} Form errors: {form.errors}')
        if form.is_valid():
            # Create a new user account
            user = form.save()
            logging.info(f'{os.getenv("ID_LOG", "")} Save a new user: {user}')
            if user is not None:
                do_login(request, user)
                return redirect('/welcome')

    return render(request, "users/register.html", {'form': form})
