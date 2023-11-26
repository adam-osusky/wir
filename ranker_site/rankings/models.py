from django.db import models
from django.contrib.auth.models import User
import json


class Task(models.Model):
    content = models.TextField()
    # type = ...

    def __str__(self):
        return self.content[:30]
    
    def content_lines(self):
        return self.content.split("\n")

class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)


class Ranking(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)
    word_order = models.TextField()

    def set_word_order(self, order):
        self.word_order = json.dumps(order)

    def get_word_order(self):
        return json.loads(self.word_order)
