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
# from controlcenter.views import controlcenter
from django.conf import settings
from django.conf.urls.static import static
from clientes.api import ClienteResource, PaisResource
from tastypie.api import Api
# from ajax_select import urls as ajax_selects_urls
# from django.contrib.auth import views as auth_views
# from clientes.admin import admin_site
# from material.frontend import urls as frontend_urls

# admin.autodiscover()
# admin.site.site_header = 'Prueba de Cabecera del Sitio'
# admin.site.site_title = 'Hola Mundo2!'
from stock.ajax import get_producto_detalle

admin.site.index_title = 'Sistema Informatico de Gestion para Bar'

# cliente_resource = ClienteResource()
v1_api = Api(api_name='v1')
v1_api.register(ClienteResource())
v1_api.register(PaisResource())


urlpatterns = [
    # url(r'^ajax_select/', include(ajax_selects_urls)),
    url(r'^$', include('clientes.urls')),
    # url(r'^$', include(admin.site.urls)),
    url(r'^compras/', include('compras.urls', namespace='compras')),
    url(r'^clientes/', include('clientes.urls')),
    url(r'^stock/', include('stock.urls', namespace='stock')),
    # url(r'^grappelli/', include('grappelli.urls')),
    url(r'^bar/', include('bar.urls', namespace='bar')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    # url(r'^admin/dashboard/', include(controlcenter.urls)),
    url(r'^sigb/', include(admin.site.urls)),
    url(r'^calendar/', include('calendarium.urls')),

    # url(r'^myadmin/', include(admin.site.urls)),
    # url(r'', include(frontend_urls)),

    # Trata de enviar la nueva contrasena por correo electronico, supongo que necesita un Servidor SMTP para el envio.
    # url(r'^admin/password_reset/$', auth_views.password_reset, name='admin_password_reset'),
    # url(r'^admin/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm,
    #     name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
