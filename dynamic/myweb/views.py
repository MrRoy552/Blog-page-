from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
from myweb.models import destination



def web(request):
    # return HttpResponse('helooo')
    # return render(request,'promena.html'),
    # dest1=destination()
    # dest1.name='pankaj'
    dest1=destination.objects.all()
    return render(request,'demo.html',{'dest1':dest1})