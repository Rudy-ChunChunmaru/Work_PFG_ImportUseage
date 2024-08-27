from django.db import models

# Create your models here.
class pib(models.Model):
    intPib_id = models.IntegerField(primary_key=True)
    strPib_numberSub = models.CharField(max_length=50,null=False,blank=False)
    strPib_dateSub = models.DateField(null=False,blank=False)
    strPib_numberReg = models.CharField(max_length=50)
    strPib_dateReg = models.DateField(null=False,blank=False)