from django.shortcuts import render,redirect,get_object_or_404
from.models import Task
# Create your views here.
def Add(request):
    task2=Task.objects.all()
    if request.method=='POST':
        slno=request.POST.get('slno','0')
        name=request.POST.get('name','')
        desc=request.POST.get('desc','')
        task=Task(slno=slno,name=name,desc=desc)
        task.save()
        # task=task.objects.all()
        
    return render(request,'home.html',{'task2':task2})
# def details(request):
#     return render(request,'detail.html',{'Task':Task})
#     task=Task.objects.all()
def delete(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,task_id1):
    task3=get_object_or_404(Task,id=task_id1)
    if request.method=='POST':
        task3.slno=request.POST.get('slno')
        task3.name=request.POST.get('name')
        task3.desc=request.POST.get('desc')
        # task=Task(slno=slno,name=name,desc=desc)
        task3.save()
        # task=task.objects.all()
        return redirect('/')
    return render(request,'update.html',{'task3':task3})

        
