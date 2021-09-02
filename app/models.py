from django.db import models

class address(models.Model):
    voter_address = models.CharField(max_length=100)