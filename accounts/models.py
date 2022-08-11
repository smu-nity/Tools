from django.contrib.auth.models import User
from django.db import models
from core.models import Information


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    information = models.ForeignKey(Information, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.information} - {self.name}'