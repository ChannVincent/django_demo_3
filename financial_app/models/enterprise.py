from django.db import models

class Enterprise(models.Model):
    name = models.CharField(max_length=200, default="")
    ticker = models.CharField(max_length=200, default="")
    description = models.TextField(null=True, blank=True)
    sector = models.CharField(max_length=200, default="")
    website = models.CharField(max_length=200, default="")
    logo_url = models.CharField(max_length=200, default="")
    share_count = models.BigIntegerField(default=0)

    class Meta:
        ordering = ["-name", "-ticker"]

    def __str__(self):
        return self.name


class Dividend(models.Model):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    price = models.DecimalField(max_digits=8, decimal_places=3)


class Share(models.Model):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    volume = models.IntegerField(default=0)


class Badge(models.Model):
    enterprises = models.ManyToManyField(Enterprise)
    title = models.CharField(max_length=200, default="")
    description = models.TextField(null=True, blank=True)
    background = models.CharField(max_length=200, default="")


    

    