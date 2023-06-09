from django.db import models


class Task(models.Model):
    content = models.TextField()
    # type = ...

    def __str__(self):
        return self.content[:30]
