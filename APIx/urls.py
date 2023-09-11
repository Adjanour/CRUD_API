from django.conf.urls import url, path
from APIx import views
from .view import personApi

urlpatterns = [
     url(r'^api$',views.personApi),
     path('api/<int:id>', personApi, name='department_api'),
]
