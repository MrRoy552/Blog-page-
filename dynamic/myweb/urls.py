from django.urls import path

from myweb import views
from myweb.views import web

urlpatterns = [

    path('', web),

]