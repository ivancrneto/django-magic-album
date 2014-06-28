from django.db import models
import jsonfield


class Album(models.Model):
    pictures = jsonfield.JSONField()


class TweetsControl(models.Model):
    since_id = models.CharField(max_length=100)
    created_on = models.DatetimeField(auto_now_add=True)
