"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BlogPostViewSet, UserViewSet, UserLoginAPIView, UserRegisterAPIView

router = DefaultRouter()
router.register(r'posts', BlogPostViewSet)
router.register(r'profile', UserViewSet)

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('', include(router.urls)),  # Include all the viewsets routes
]
