from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from user.models import User
# Create your views here.
def crud_task(request):
    if request.method == 'GET':
        if request.session.get('useremail'):
            email_session = request.session.get('useremail')
            print('welcome')
            # tasks = Task.objects.all()

            user_obj = User.objects.get(email = email_session)
        
            tasks = Task.objects.filter(user = user_obj).order_by('-created_at')
        
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
    
def update_task(request):
    
    if request.method == 'POST':
        print("Do update")
        task_id = request.POST.get("task_id")
        task_name_updated = request.POST.get("task_name_updated")
        task_description_updated = request.POST.get("task_name_description_updated")
        
        task_update_obj = Task.objects.get(id = task_id)
        task_update_obj.title = task_name_updated
        task_update_obj.description = task_description_updated
        task_update_obj.save()
        
        return redirect('/task/crud')  
    else:
        return HttpResponse("post method needed")    
    
def single_view(request, **kwargs):
    print(kwargs)
    task_id = kwargs['id']
    taskobj = Task.objects.get(id = task_id)
    
    return render(request, 'todotask/single_view.html', {'task':taskobj})

def delete_view(request, id):
    obj = Task.objects.get(id = id)
    obj.delete()
    return redirect('/task/crud')                      