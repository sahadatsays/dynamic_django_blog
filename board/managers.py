from django.db import models

class PrimaryNavManager(models.Model):
     def get_queryset(self):
          return super().get_queryset().filter(parent=None)

class SubNavManager(models.Model):
     def get_queryset(self):
          return super().get_queryset().exclude(parent=None)