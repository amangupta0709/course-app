from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(
        User, null=True, blank=True, related_name="student_courses"
    )
    educator = models.ForeignKey(User, related_name="educator_courses")
