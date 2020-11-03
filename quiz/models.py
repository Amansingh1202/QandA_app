from django.db import models
from django.conf import settings
class Scores(models.Model):
    score = models.IntegerField()
    date = models.DateField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
        )

    def __str__(self):
        return '{} -> {}'.format(self.user, self.score)
        

