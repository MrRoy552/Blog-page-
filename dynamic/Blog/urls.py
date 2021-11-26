from django.urls import path

from Blog.views import blogpage, savedata, login, register, getdata, logout, comment_message
from myweb import views



urlpatterns = [
    path('register',register),
    path('savedata', savedata),
    path('getdata', getdata),
    path('login', login),
    path('blog', blogpage),
    path('logout', logout),
    path('cmnt_message',comment_message)
]