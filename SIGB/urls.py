"""SIGB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
# from django.contrib.auth import views as auth_views
# from clientes.admin import admin_site
# from material.frontend import urls as frontend_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^myadmin/', include(admin.site.urls)),
    # url(r'^clientes/', include('clientes.urls')),
    # url(r'', include(frontend_urls)),

    # Trata de enviar la nueva contrasena por correo electronico, supongo que necesita un Servidor SMTP para el envio.
    # url(r'^admin/password_reset/$', auth_views.password_reset, name='admin_password_reset'),
    # url(r'^admin/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm,
    #     name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
