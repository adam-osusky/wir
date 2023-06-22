from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .models import Task
from .task_assignment import get_task


def task_detail(request):
    user_id = request.user.id
    task_pk = get_task(user_id)
    context = {'task': Task.objects.get(pk=task_pk), 'user_id': user_id}
    return render(request, 'rankings/task_detail.html', context)


def submit_task(request):
    if request.method == 'POST':
        # Parse the JSON data from the request
        # order_data = request.json
        order_data = json.loads(request.body)

        # Extract the necessary data
        user_id = order_data.get('userId')
        task_id = order_data.get('taskId')
        word_order = order_data.get('selectedWords')
        print(word_order)

        # TODO save the word order into the db
        # TODO check if taskid-userid already submitted
        # get score of submition
        score = calculate_score(word_order)

        return JsonResponse({'score': score})

    # Handle other HTTP methods if necessary
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


# score task view
def score_task(request):
    task_id = request.GET.get('task_id')
    score = request.GET.get('score')
    # user_id = request.user.id

    # Perform any additional processing with the data
    # TODO maybe show optimal word ordering

    # Render the new page with the necessary context
    context = {
        'task_id': task_id,
        'score': score,
    }
    return render(request, 'rankings/score_task.html', context)


def calculate_score(word_order):
    # scoring function
    score = len(word_order)  # TODO
    return score
