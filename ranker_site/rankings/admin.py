from django.contrib import admin
from .models import Task, Assignment, Ranking


admin.site.register(Task)
admin.site.register(Assignment)
admin.site.register(Ranking)
