from django.db import models
import jsonfield


class Album(models.Model):
    pictures = jsonfield.JSONField()
