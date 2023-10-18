"""buy_and_sell URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from advertisement.views import Register, EmailVerify
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('advertisement.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('register/confirm_email/', TemplateView.as_view(
        template_name='registration/confirm_email.html'), name='confirm_email'),
    path('register/confirm/', EmailVerify.as_view(), name='confirm'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)