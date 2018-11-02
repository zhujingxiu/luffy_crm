"""luffy_crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from xstark.sites import site
from system import views as system_view
from home.views import auth, home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('rbac/', include('rbac.urls', namespace='rbac')),

    path('xstark/', site.urls),
    path('xstark/login/', system_view.login),
    path('xstark/logout/', system_view.logout),
    path('xstark/profile/', system_view.profile),
    path('xstark/dashboard/', system_view.dashboard),

    path('login/', auth.login, name='login'),
    path('logout/', auth.logout, name='logout'),
    path('home/', home.IndexView.as_view(), name='index'),
    path('my/', include('home.urls', namespace='home')),
]
