from .models import Ranking
from Levenshtein import distance


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
        return 1

    # Compute the final score as the inverse of the average distance
    final_score = 1 / (sum_dist / num_rankings)
    print((sum_dist / num_rankings))

    return final_score

