"""
URL configuration for proyecto project.

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
from django.urls import path
from aplicacion.views import inicioPeli
from aplicacion.views import verPeli1
from aplicacion.views import verPeli2
from aplicacion.views import verPeli3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicioPeli, name="inicio"),
    path('verPeli1/', verPeli1, name="verPeli1"),
    path('verPeli2/', verPeli2, name="verPeli2"),
    path('verPeli2/', verPeli3, name="verPeli3")
]
#No me cargo nunca el {% static load %}