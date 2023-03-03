from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import TaskStatus, DEFAULT_STATUS, \
    TaskSection, DEFAULT_SECTION


@receiver(post_save, sender=get_user_model())
def create_default_task_status(sender, instance, created, **kwargs):
    if created:
        TaskStatus.objects.create(
            user=instance,
            **DEFAULT_STATUS
        )
        TaskSection.objects.create(
            user=instance,
            **DEFAULT_SECTION
        )
