from django.shortcuts import render, redirect, reverse
from system.models import UserInfo
from django.contrib.auth.hashers import check_password
from django.conf import settings
# Create your views here.


def login(request):
    if request.method == "GET":
        return render(request, 'system/login.html')

    username = request.POST.get('user')
    pwd = request.POST.get('pwd')
    user = UserInfo.objects.filter(username=username).first()
    if not user or not user.password or not check_password(pwd, user.password):
        return render(request, 'system/login.html', {'msg': '用户名或密码错误'})

    # 用户名和密码正确,用户信息放入session
    request.session['user_info'] = {'id': user.id, 'name': user.name}

    return redirect(settings.XSTARK_HOME)


def logout(request):
    if request.session.get('user_info'):
        del request.sesssion['user_info']
    return redirect(settings.XSTARK_ENTRANCE)


def profile(request):

    return render(request, 'system/profile.html', {})


def dashboard(request):
    return render(request, 'system/dashboard.html', {})