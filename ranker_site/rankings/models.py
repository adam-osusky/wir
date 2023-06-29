from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    content = models.TextField()
    # type = ...

    def __str__(self):
        return self.content[:30]


class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)


class Ranking(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)
    word_order = models.TextField()  # TODO same words at different position - differentiate

    def set_word_order(self, string_list):
        self.word_order = " ".join(string_list)

    def get_word_order(self):
        return self.word_order.split(" ")
