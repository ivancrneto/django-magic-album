from django.db import models
from django.db.models.signals import post_save
from .utils import send_album_email
import jsonfield


class Album(models.Model):
    pictures = jsonfield.JSONField()

    def add_picture(self, picture):
        if not self.pictures:
            # by default jsonfeld returns an empty dict instead of list
            self.pictures = [picture]
        else:
            self.pictures.append(picture)

        self.save()

post_save.connect(send_album_email, sender=Album)


class TweetsControl(models.Model):
    since_id = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_last_since_id(cls):
        if not cls.objects.count():
            return 0
        return int(cls.objects.order_by('-created_on')[0].since_id)
