__author__ = 'pmmr'

from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource
from .models import Cliente
from bar.models import Pais


class PaisResource(ModelResource):
    class Meta:
        queryset = Pais.objects.all()
        resource_name = 'pais'


class ClienteResource(ModelResource):

    pais = fields.ForeignKey(PaisResource, 'pais')

    class Meta:
        queryset = Cliente.objects.all()
        resource_name = 'cliente'
        authorization = Authorization()
        excludes = ['email']
        # fields = []
        allowed_methods = ['get']