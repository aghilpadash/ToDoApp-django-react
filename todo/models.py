from datetime import datetime

from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now(), blank=False)

    def _str_(self):
        return self.title
