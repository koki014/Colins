
from django.db.models.signals import post_save
from django.dispatch import receiver
from slugify import slugify

from .models import Category

@receiver(post_save, sender=Category)
def create_user_profile(sender, instance, created, **kwargs):
    instance.slug = slugify(instance.title )
    

