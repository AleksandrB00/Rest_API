import random
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class GoodsModel(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField()
    price = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

class CheckModel(models.Model):

    def number():
        count = CheckModel.objects.count()
        if count == None:
            return 1
        else:
            return count + 1

    check_id = models.CharField(unique=True, max_length=1000, default=number)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField()

    def __str__(self):
        return self.balance

class TransactionModel(models.Model):

    def number():
        count = TransactionModel.objects.count()
        if count == None:
            return 1
        else:
            return count + 1

    transaction_id = models.ForeignKey(CheckModel, on_delete=models.CASCADE, unique=True, default=number)
    money = models.IntegerField()
    transaction_date = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.transaction_id

class Profile(models.Model):

    def get_conf_code():
        code = random.randint(100000, 900000)
        return code

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    conf_code = models.IntegerField(default=get_conf_code)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()