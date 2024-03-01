from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from rankings.scoring_funcs import refresh_overall_score


class Command(BaseCommand):
	help = 'Update leaderboard scores fro every user.'
	
	def handle(self, *args, **kwargs):
		users = User.objects.filter(is_superuser=False).values_list('id', flat=True)
		
		for user in users:
			refresh_overall_score(user)
		
		self.stdout.write(f'Job done')
