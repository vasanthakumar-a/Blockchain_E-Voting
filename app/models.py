from django.db import models

class addressDB(models.Model):
    voter_address = models.CharField(max_length=100)

class authoDB(models.Model):
    auth = models.IntegerField()
    auth_address = models.CharField(max_length=100)