from rankings.models import Task, Assignment
from django.contrib.auth.models import User


def add_assignments_for_user(user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        print(f"User with ID {user_id} does not exist.")
        return

    tasks = Task.objects.all()

    for task in tasks:
        # Check if the assignment already exists for this user and task
        if not Assignment.objects.filter(user=user, task=task).exists():
            assignment = Assignment(user=user, task=task, is_completed=False)
            assignment.save()
            print(f"Assignment created for user '{user.username}' for task: '{task}'.")
