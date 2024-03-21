from django.db import models
from django.urls import reverse

# Create your models here.


class Companies(models.Model):
    # Meta tag is so django doesn't prepend the app name('frontend_companies')
    class Meta:
        db_table = 'companies'
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Stocks(models.Model):
    class Meta:
        unique_together = ('date', 'type')
        db_table = 'stocks'
    type = models.ForeignKey(Companies, on_delete=models.CASCADE)
    date = models.IntegerField(null=False)
    open = models.FloatField(default=0)
    high = models.FloatField(default=0)
    low = models.FloatField(default=0)
    close = models.FloatField(default=0)
    adj_close = models.FloatField(default=0)
    volume = models.FloatField(default=0)

class Simulations(models.Model):
    class Meta:
        db_table = 'simulations'
    strategy = models.CharField(max_length=100, default='')

class Images(models.Model):
    class Meta:
        db_table = 'images'
    image = models.ImageField(upload_to='', default=None)

class Results(models.Model):
    class Meta:
        db_table = 'results'
    simulation = models.ForeignKey(Simulations, on_delete=models.CASCADE, null=False)
    image = models.ForeignKey(Images, on_delete=models.CASCADE, null=False)

    def get_absolute_url(self):
        return reverse('result_detail', kwargs={'result_id': self.id})
        # return reverse('result_detail', args=[str(self.id)])


