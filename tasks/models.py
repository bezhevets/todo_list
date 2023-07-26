from django.db import models
from django.utils.timezone import now


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True, default=now)
    is_completed = models.BooleanField(default=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content} {self.is_completed}"
