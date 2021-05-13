from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=200)
    def __str__(self):
       return self.country_name


class Cases(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    confirmed_cases = models.IntegerField(default=0)
    death_cases = models.IntegerField(default=0)
    recovery_cases = models.IntegerField(default=0)
    def __str__(self):
       country_name = str(self.country)
       return "Cases in " +  country_name