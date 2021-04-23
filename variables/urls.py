from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

from . import views

urlpatterns = [
    path('variables/', views.variable_list, name='variableList'),
    path('variable/<id>', views.single_variable, name='singleVariable'),
    path('variablecreate/', csrf_exempt(views.variable_create), name='variableCreate'),
]
