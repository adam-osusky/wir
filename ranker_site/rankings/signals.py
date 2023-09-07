from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rankings.prepare_data_utils import add_assignments_for_user

@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        add_assignments_for_user(instance.id)
