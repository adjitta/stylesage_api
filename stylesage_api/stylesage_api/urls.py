"""stylesage_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from music.views import get_artist, get_albums
from passphrase_validation.views import get_basic_passphrase_validation, get_advanced_passphrase_validation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artists/', get_artist),
    path('albums/', get_albums),
    path('passphrase/basic/', get_basic_passphrase_validation),
    path('passphrase/advanced/', get_advanced_passphrase_validation)

]
