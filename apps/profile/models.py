from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField('first_name', max_length=255, blank=True, null=True)
    last_name = models.CharField('last_name ', max_length=255, blank=True, null=True)
    email = models.EmailField('email ', max_length=255, blank=True, null=True)
    phone = models.CharField('phone', max_length=20, blank=True)
    company = models.CharField('company ', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
