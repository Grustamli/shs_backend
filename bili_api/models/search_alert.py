from django.db import models
from django.contrib.auth.models import User

class SearchAlert(models.Model):
    search_term     = models.CharField(max_length=150)
    owner           = models.ForeignKey(User, related_name="search_alert")
    notify          = models.BooleanField(default=True)
    def __str__(self):
        return self.search_term
    class Meta:
        unique_together = ('owner', 'search_term')
