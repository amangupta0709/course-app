# from django.contrib.auth.models import Group, User
# from django.db import models


# class StudentManager(models.Manager):
#     def get_query_set(self):
#         return self.filter(groups__name="Student")


# class EducatorManager(models.Manager):
#     def get_query_set(self):
#         return self.filter(groups__name="Educator")


# class Student(User):
#     class Meta:
#         proxy = True

#     objects = StudentManager()

#     def save(self, *args, **kwargs):
#         super(Student, self).save(*args, **kwargs)
#         if not self.groups.filter(name="Student").exists():
#             group, created = Group.objects.get_or_create("Student")
#             self.groups.add(group)


# class Educator(User):
#     class Meta:
#         proxy = True

#     def save(self, *args, **kwargs):
#         super(Educator, self).save(*args, **kwargs)
#         if not self.groups.filter(name="Educator").exists():
#             group, created = Group.objects.get_or_create("Educator")
#             self.groups.add(group)
