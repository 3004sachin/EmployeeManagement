from django.shortcuts import render,redirect
from . models import *
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')



def add_employee(request):
    if request.method=="POST":
        employee_name=request.POST['employeename']
        employee_profile=request.POST['employeeprofile']
        department=request.POST['department']
        location=request.POST['location']
        phone=request.POST['phone']
        salary=request.POST['salary']
        bonus=request.POST['bonus']
        role=request.POST['role']
        Employees.objects.create(employee_name=employee_name,employee_profile=employee_profile,location=location,department=department,phone=phone,salary=salary,role=role,bonus=bonus)
    return render(request,'employee.html')




def all_employee(request):
    data=Employees.objects.all()
    context={"data":data}
    return render(request,'all_employee.html',context)

def remove_employee(request,id):
    data=Employees.objects.get(id=id).delete()
    return redirect('all_employee')


def Edit_employee(request,id):
    data=Employees.objects.get(id=id)
    IT='IT'
    Medical='Medical'
    Business='Business'
    if data.department=='IT':
        context={'data':data,'IT':IT}
    elif data.department=='Medical':
        context={'data':data,'Medical':Medical} 
    elif data.department== 'Business':
        context={'data':data,'Business':Business} 
    if data:    
        if request.method=='POST':
            employee_name=request.POST['employeename']
            employee_profile=request.POST['employeeprofile']
            department=request.POST['department']
            location=request.POST['location']
            phone=request.POST['phone']
            salary=request.POST['salary']
            bonus=request.POST['bonus']
            role=request.POST['role']  
            data.employee_name=employee_name
            data.employee_profile=employee_profile
            data.department=department
            data.location=location
            data.phone=phone
            data.salary=salary
            data.bonus=bonus
            data.role=role
            data.save()
            return redirect('all_employee')         
    return render(request,'update_employee.html',context)

 

        


