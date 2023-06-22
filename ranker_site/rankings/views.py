from django.shortcuts import render
from django.http import JsonResponse
from .models import Task


def task_detail(request, pk):
    context = {'task': Task.objects.get(pk=pk), 'user_id': request.user.id}
    return render(request, 'rankings/task_detail.html', context)
