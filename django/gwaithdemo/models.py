from django.db import models


class Rate(models.Model):
    date = models.DateTimeField()
    rate = models.FloatField()
    currency = models.CharField(max_length=3)

    class Meta:
        unique_together = ('date', 'rate', 'currency')
