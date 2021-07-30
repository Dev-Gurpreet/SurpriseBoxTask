from django.db import models
from django.contrib.auth.models import User

class Subscriber(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    subscribe = models.BooleanField(default=False,null=True, blank=True)
    visitCount = models.IntegerField(default=0, null=True, blank=True)
    winner = models.BooleanField(default=False,null=True, blank=True)


    @property
    def get_subscribe_Button(self):
        if self.subscribe == True:
            return 'Unsubscribe'
        return 'Subscribe'

# Create your models here.
