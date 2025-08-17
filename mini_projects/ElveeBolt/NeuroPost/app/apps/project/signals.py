from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ProjectPlan
from .tasks import create_project_plan

@receiver(post_save, sender=ProjectPlan)
def on_project_plan_created(sender, instance, created, **kwargs):
    if created and instance.is_gpt is True:
        create_project_plan.delay(plan_id=instance.pk)