from django.shortcuts import render
from webapp.models import Task, status_choices
from django.http import HttpResponseRedirect


def index_view(request):
    tasks = Task.objects.all()
    return render(request, template_name='index.html', context={'tasks': tasks})


def task_create_view(request):
    if request.method == 'GET':
        return render(request, template_name='task_create.html', context={'status_choices': status_choices})
    elif request.method == 'POST':
        Task.objects.create(
            description=request.POST.get('description'),
            status=request.POST.get('status'),
            date_of_finish=request.POST.get('date_of_finish')
        )
        return HttpResponseRedirect('/')


def task_delete_view(request):
    if request.method == "POST":
        task_id = request.POST.get("id")
        task = Task.objects.get(id=task_id)
        task.delete()
        return HttpResponseRedirect('/')
