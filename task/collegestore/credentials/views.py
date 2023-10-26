from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render

from .models import Course,Student,Purpose

from . forms import  StudentForm
from collegestoreapp.models import Department


def login(request):
    # next = ""
    #
    # if request.GET:
    #     next = request.GET['new']
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)

            return render(request,'new.html')

        else:
            messages.info(request,"invalid credentials")
            return redirect('credentials:login')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('credentials:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('credentials:register')
            else:
                 user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                 user.save();
                 return redirect('credentials:login')



        else:
              messages.info(request,"password is not matching")
              return redirect('credentials:register')


    else:
        return render(request,"register.html")

def new(request):
    return render(request,'new.html')

def student_create(request):
 form=StudentForm()
 if request.method == 'POST':
     form=StudentForm(request.POST)
     if form.is_valid():
         form.save()
         messages.info(request,"your order is placed")
         return redirect('credentials:student_add')
 return render(request,'form.html',{'form':form})


def student_update(request,pk):
    student=get_object_or_404(Student,pk=pk)
    form=StudentForm(instance=student)
    if request.method == 'POST':
       form=StudentForm(request.POST,instance=student)
       if form.is_valid():
           form.save()
           return redirect('student_change',pk=pk)
    return render(request,'form.html',{'form':form})



def get_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return JsonResponse(list(courses.values('id', 'name')),safe=False)
    # return render(request,'courses_dropdown_list.html',{'courses':courses})



