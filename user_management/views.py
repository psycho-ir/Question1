from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
from random import choice
from user_management.models import User
from user_management.user_manager import register_user, CaptchaException, UserAlreadyExistException, authenticate

captcha_options = ['wow', 'hello', 'geek', 'nerd', 'yagni']


class LoginView(View):
    def get(self,request):
        return render_to_response('login.html',{},RequestContext(request))

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        return HttpResponse(authenticate(username, password))


class RegisterView(View):
    def get(self, request):
        captcha = choice(captcha_options)
        request.session['captcha'] = captcha

        return render_to_response('register.html', {'captcha': captcha}, RequestContext(request))

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        captcha = request.POST['captcha']
        user = User()
        user.username = username
        user.email = email
        user.set_password(password)
        try:
            register_user(user, captcha, request.session)
            return HttpResponse("You registered")
        except CaptchaException as e:
            return HttpResponse("Captcha is wrong")
        except UserAlreadyExistException as e:
            return HttpResponse("User already exists")
        except Exception as e:
            return HttpResponse(e)


