from django.db import models
from django.contrib.auth.models import User
from ..custom_fields.lowercase_char_field import LowerCaseCharField

class SearchAlert(models.Model):
    search_term     = LowerCaseCharField(max_length=150)
    owner           = models.ForeignKey(User, related_name="search_alerts")
    notify          = models.BooleanField(default=True)
    def __str__(self):
        return self.search_term

    def save(self, *args, **kwargs):
        self.search_term = self.search_term.lower()
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('owner', 'search_term')
