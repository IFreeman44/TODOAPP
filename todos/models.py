from django.db import models
from django.conf import settings


class Todo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    todo_date = models.DateField()
    todo_start_time = models.TimeField(null=True)
    todo_end_time = models.TimeField(null=True)
    todo_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.email
    





