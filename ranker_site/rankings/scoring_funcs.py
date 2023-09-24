from Levenshtein import distance
from .models import User, Ranking, Assignment
from users.models import UserProfile


def levenshtein(word_order, task_id):
    # Retrieve all the Ranking instances for the given task_id
    rankings = Ranking.objects.filter(assignment__task_id=task_id)
    positions = [item['position'] for item in word_order]  # {word, position}

    scores = []
    for ranking in rankings:
        current_positions = [item['position'] for item in ranking.get_word_order()]
        lev_distance = distance(positions, current_positions)
        scores.append(lev_distance)

    sum_dist = sum(scores)
    num_rankings = len(scores)

    # fail safe
    if sum_dist == 0:
        return 0

    # Compute the final score as the inverse of the average distance
    avg_dist = (sum_dist / num_rankings)
    # final_score = int(avg_dist)
    final_score = 1 / avg_dist
    final_score = int(final_score * 100)
    print(avg_dist)

    return final_score


def refresh_overall_score(user_id):
    try:
        user = User.objects.get(pk=user_id)
        assignments_of_user = Assignment.objects.filter(user=user)
        score = 0
        for assignment in assignments_of_user:
            if not assignment.is_completed:
                continue
            ranking = Ranking.objects.get(assignment=assignment)
            task_id = assignment.task.pk
            word_order = ranking.get_word_order()
            score += levenshtein(word_order, task_id)
        profile = UserProfile.objects.get(user=user)
        profile.score = score
        profile.save()

    except User.DoesNotExist:
        pass

