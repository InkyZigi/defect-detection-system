"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from . import views

app_name = "detection"

urlpatterns = [
    path('', views.dashborad, name='index'),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    path('index/', views.dashborad),
    path('card/', views.card),
    path('chart/', views.chart),
    path('coreui/dist/<str:html>/', views.shift),
]

# user management
urlpatterns += [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('user/profile/', views.profile, name='profile'),
    path('user/organization/', views.organization, name='organization'),
    path('user/settings/', views.settings, name='settings'),
    path('user/authority/', views.authority, name='authority'),

]

# work
urlpatterns += [
    path('work/model/', views.model, name='model'),
    path('work/sheet/', views.sheet, name='sheet'),
    path('work/sheet/op/', views.sheet_op, name='sheet_op'),
]

# models
urlpatterns += [
    path('v1/', views.model),
]

# upload
urlpatterns += [
    re_path(r'media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
]