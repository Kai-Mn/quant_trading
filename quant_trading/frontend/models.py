from django.db import models

# Create your models here.


class Companies(models.Model):
    name = models.CharField(max_length=4, unique=True)

    def __self__(self):
        return self.name


class Stocks(models.Model):
    class Meta:
        db_table = 'frontend_stocks'
    type = models.ForeignKey(Companies, on_delete=models.CASCADE)
    date = models.IntegerField(null=False)
    open = models.FloatField(default=0)
    high = models.FloatField(default=0)
    low = models.FloatField(default=0)
    close = models.FloatField(default=0)
    adj_close = models.FloatField(default=0)
    volume = models.FloatField(default=0)
