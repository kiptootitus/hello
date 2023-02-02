from django.db import models

class myapp(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  
# myapp2=myapp(firstname='Tobias', lastname='Refsnes', phone='0705839228',joined_date='2023-03-04')
# myapp3=myapp(firstname='Meshack', lastname='Kibiwott', phone='0100436617',joined_date='2022-11-04')    
# myapp4=myapp(firstname='Brian', lastname='Kibet', phone='0700436617',joined_date='2020-11-04')    