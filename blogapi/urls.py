"""blogapi URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.views import BlogViewSet, CommentViewSet

router = DefaultRouter()
router.register('blog', BlogViewSet)
router.register('comment', CommentViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('dj_rest_auth.urls')), #로그인, 로그아웃 기능
    path('accounts/register/', include('dj_rest_auth.registration.urls')), #회원가입 기능
    path('accounts/', include('accounts.urls')),
    path('', include(router.urls)), #localhost:8000/blog/
]
