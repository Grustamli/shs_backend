from django.db import models
from django.contrib.auth.models import User

class SearchAlert(models.Model):
    search_term     = models.TextField()
    owner           = models.ForeignKey(User, related_name="search_alert")
    notify          = models.BooleanField(default=True)
