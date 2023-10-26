
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from . models import Department

def home(request):
    result=Department.objects.all()
    context={'result':result

             }
    return render(request,'home.html',context)

def alldepdetails(request,pk):

         department=get_object_or_404(Department,pk=pk)
         return render(request,'department.html',{'res':department})


