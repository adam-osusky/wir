from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .models import Task, Assignment, User, Ranking
from .task_assignment import get_task
from .scoring_funcs import levenshtein


def task_detail(request):
    user_id = request.user.id
    task_pk = get_task(user_id)
    if task_pk:
        context = {'task': Task.objects.get(pk=task_pk), 'user_id': user_id}
        return render(request, 'rankings/task_detail.html', context)
    else:
        # no unfinished assignments
        return render(request, 'users/dashboard.html')


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

        assignment = find_assignment(user_id, task_id)
        if assignment:
            # TODO update the mean of rankings

            # get the score of submition
            score = calculate_score(word_order, task_id)

            # save the word order into the db
            ranking = Ranking(assignment=assignment, score=score)
            ranking.set_word_order(word_order)
            ranking.save()

            assignment.is_completed = True
            assignment.save()

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


def calculate_score(word_order, task_id):
    score = levenshtein(word_order, task_id)
    return score


def find_assignment(user_id, task_id):
    try:
        user = User.objects.get(id=user_id)
        task = Task.objects.get(id=task_id)
        assignment = Assignment.objects.get(user=user, task=task)
        return assignment
    except Assignment.DoesNotExist:
        return None

# def process_word_order(wo):
#     """Give every word its rank and add unselected words with the same last rank"""
#     for i, w in enumerate(wo):
#         w['rank'] = i
#     return wo
