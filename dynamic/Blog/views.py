from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
# def register(request):
#     if request.method=='POST':
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/login')
#     else:
#         form=UserCreationForm()
#     return render(request,'register.html',{'form':form})
from django.contrib.auth.models import User,auth

# from Blog.models import user_register
from Blog.models import comment


def register(request):
    return render(request,'register.html')

def savedata(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password1, email=email,
                                    first_name=first_name, last_name=last_name)
        user.save()
    return render(request, 'login.html')
    # return render(request,'register.html')
    # if request.method=='POST':
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     confirm_password = request.POST['confirm_password']
    #     user=User.objects.create_user(name=name,password=password,email=email)
    #     user.save()
    #     print('user created')
    #     if password==confirm_password:
    #         return redirect('register')

            # if User.objects.filter(username=username).exits():
         # return render(request,'register.html',name=name,email=email,password=password,confirm_password=confirm_password)
def login(request):
    return render(request,'login.html')

def getdata(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'Blog.html')

        else:
            messages.info(request, 'invalid credentials')
            return render(request, 'login.html')
    # data=user_register()
    # data.name=request.POST['name']
    # data.email=request.POST['email']
    # data.password=request.POST['password']
    # data.confirm_password=request.POST['confirm_password']
    # if password == confirm_password:
    # data.save()
    # messages.info(request,"You are now registered ")
    # # obj = user_register.objects.all()
    # print(data)
    # return render(request, 'login.html')
    # return render(request,'register.html',{'obj':obj})




# def getdata(request):
    # if request.method=='POST':
    #     data = user_register(request,request.POST)
    #     if data.is_valid():
    #         data.name = request.GET['name']
    #         data.email = request.GET['email']
    #         data.password = request.GET['password']
    #         # if data.password==data.password:
    #         #     return render(request,'Blog.html')
    #         # else:
    #         return render(request,'Blog.html')

def blogpage(request):
    return render(request,'Blog.html')

def logout(request):
    return render(request,'demo.html')
    # return HttpResponse('helllloooo')
def comment_message(request):
    cmt_message=comment()
    cmt_message.name=request.POST['author']
    cmt_message.msg=request.POST['msg']
    cmt_message.save()
    return render(request,'Blog.html')
