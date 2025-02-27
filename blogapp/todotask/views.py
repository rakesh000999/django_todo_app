from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from user.models import User
# Create your views here.
def crud_task(request):
    if request.method == 'GET':
        if request.session.get('useremail'):
            print('welcome')
            tasks = Task.objects.all()
            data = {'Welcome':'Hello user!', 'data':tasks}
            
            return render(request, 'todotask/crud_task.html', data)
        else:
            return redirect('user/login/')    
    
    if request.method == 'POST':
        print('Do post operation')
        task_name = request.POST.get('task_name')
        task_description = request.POST.get('task_description')
        useremail = request.session.get('useremail')
        user_obj = User.objects.get(email = useremail)
        task = Task.objects.create(title = task_name, description = task_description, user = user_obj)
        return redirect('/task/crud')
            