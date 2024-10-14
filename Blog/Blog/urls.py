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
from django.contrib import admin
from django.urls import path,include
#  to display the image in the website
from django.conf import settings
from django.conf.urls.static import static
from app import views
from rest_framework.authtoken import views as rviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('app.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', rviews.obtain_auth_token),
    path('user_logout', views.user_logout.as_view()),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#  imported include and added the url path to all the apps - before that we created app ulrs and import views and add path of view

