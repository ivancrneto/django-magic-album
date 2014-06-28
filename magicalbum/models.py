from django.db import models
import jsonfield


class Album(models.Model):
    pictures = jsonfield.JSONField()


class TweetsControl(models.Model):
    since_id = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def get_last_since_id(self):
        if not self.objects.count():
            return 0
        return int(self.objects.order_by('-created_on')[0].since_id)
