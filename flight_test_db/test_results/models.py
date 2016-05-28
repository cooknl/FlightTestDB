from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TestResult(models.Model):
    location = models.CharField(