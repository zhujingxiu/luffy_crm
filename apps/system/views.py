from django.shortcuts import render, redirect, reverse
from system.models import UserInfo
from rbac.service.init_permission import init_permission
from django.contrib.auth.hashers import check_password

# Create your views here.


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    username = request.POST.get('user')
    pwd = request.POST.get('pwd')
    user = UserInfo.objects.filter(username=username).first()
    if not user or not user.password or not check_password(pwd, user.password):
        return render(request, 'login.html', {'msg': '用户名或密码错误'})

    # 用户名和密码正确,用户信息放入session
    request.session['user_info'] = {'id': user.id, 'name': user.name}

    # 权限信息初始化
    init_permission(user, request)

    return redirect(reverse('xstark:service_student_changelist'))


def logout(request):

    request.session.clear()
    return redirect('/login')