from django.conf.urls import url
from django.urls import path
from APIx import views
from APIx.views import personApi

urlpatterns = [
     url(r'^api$',views.personApi),
     path('api/<int:id>', personApi, name='person_api'),
]
