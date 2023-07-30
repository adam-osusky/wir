import random
from django.contrib.auth.models import User
from rankings.models import Task, Assignment


def get_task(user_id):
    try:
        # Retrieve the assignments for the given user that are not completed
        assignments = Assignment.objects.filter(user_id=user_id, is_completed=False)

        # If no not completed assignments found, return None
        if not assignments:
            return None

        # Return a random assignment from the list of not completed assignments
        assignment = random.choice(assignments)
        return assignment.task.id

    except User.DoesNotExist:
        # Handle the case when the user does not exist
        return None
