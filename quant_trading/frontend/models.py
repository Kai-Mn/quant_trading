from django.db import models
from django.urls import reverse

# Create your models here.


class Companies(models.Model):
    # Meta tag is so django doesn't prepend the app name('frontend_companies')
    class Meta:
        db_table = 'companies'
    name = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.name

class Stocks(models.Model):
    class Meta:
        db_table = 'stocks'
    type = models.ForeignKey(Companies, on_delete=models.CASCADE)
    date = models.IntegerField(null=False)
    open = models.FloatField(default=0)
    high = models.FloatField(default=0)
    low = models.FloatField(default=0)
    close = models.FloatField(default=0)
    adj_close = models.FloatField(default=0)
    volume = models.FloatField(default=0)
    