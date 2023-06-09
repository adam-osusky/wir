from django.shortcuts import render
from .models import Task


def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    context = {'task': task}
    return render(request, 'rankings/task_detail.html', context)
