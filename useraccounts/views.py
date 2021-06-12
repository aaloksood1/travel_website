from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth

from .models import UserOperations
from . import urls

# Create your views here.

REGISTER_HTML = 'useraccounts/register.html'
LOGIN_HTML = 'useraccounts/login.html'

def register(request):
    return render(request, REGISTER_HTML)


def add_new_user(request):
    print("Adding new user -- Yay!")
    #print(request.POST)
    user_data = request.POST
    # check for various user data validations, should happend at model level

    # extract all user data
    username = user_data['username']
    password = user_data['password1']
    confirm_password = user_data['password2']
    first_name = user_data['first_name']
    last_name = user_data['last_name']
    email = user_data['email']

    # Call the static method of  the Appusers class to create user
    user, errors = UserOperations.create_a_user(username = username,
                                    email = email,
                                    first_name = first_name,
                                    last_name=last_name,
                                    password= password,
                                    confirm_password=confirm_password)

    # if errors is not empty, it implies that user could not be created successfully
    # if errors is empty, the user was created successfully and we get the user object back too
    # is user was created successfully, send to home page with user logged in
    # else send back to login back with error message
    if errors:
        print("user not created due to errors: {}".format(errors))
        for error in errors:
                messages.add_message(request, messages.ERROR, error)
        redirect_to = urls.REGISTER_PAGE
    else:
        #messages.add_message(request, messages.INFO, "User {} created successfully".format(username))
        print("user with username {} created".format(username))
        #auth.login(request, user )
        #return redirect('/')
        #do_login(request)
        redirect_to = _do_login(request = request,
                                username = username,
                                password = password)

    return redirect(redirect_to)


def login(request):
    return render(request, LOGIN_HTML)

def _do_login(request, username, password):
    user = UserOperations.authenticate_user(username = username,
                                            password= password)

    # is user was created successfully, send to home page with user logged in
    # else send back to login back with error message
    if user:
        auth.login(request, user)
        redirect_url = urls.HOMEPAGE
    else:
        messages.add_message(request, messages.ERROR, "Incorrect username and password combination")
        redirect_url = urls.LOGIN_PAGE

    return redirect_url

def do_login(request):
    login_data = request.POST
    username = login_data["username"]
    password = login_data["password"]
    print("login requested {} , {}".format(username, password))
    redirect_to = _do_login(request = request,
                            username = username,
                            password = password)
    return redirect(redirect_to)


def do_logout(request):
    #do user logout here
    auth.logout(request)
    print("logout requested")
    #send back to home page
    redirect_to = urls.HOMEPAGE
    return redirect(redirect_to)