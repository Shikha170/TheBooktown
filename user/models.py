from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=120)
    mobile=models.CharField(max_length=20)
    message=models.CharField(max_length=600)
    def __str__(self):
        return self.email

class category(models.Model):
    cname=models.CharField(max_length=40)
    cpic=models.ImageField(upload_to='static/category/',default="")
    cdate=models.DateField()

    def __str__(self):
        return self.cname

class profile(models.Model):
    name=models.CharField(max_length=120)
    dob = models.DateField(max_length=20)
    mobile=models.CharField(max_length=20)
    email=models.EmailField(max_length=80,primary_key=True)
    passwd=models.CharField(max_length=100)
    ppic=models.ImageField(upload_to='static/profile/',default="")
    address=models.TextField(max_length=2000)

class login(models.Model):
    email=models.CharField(max_length=30,primary_key=True)
    passwd=models.CharField(max_length=20)

class product(models.Model):
    name=models.CharField(max_length=150)
    ppic=models.ImageField(upload_to='static/products',default="")
    language=models.CharField(max_length=40)
    hardcover=models.CharField(max_length=50)
    publisher=models.CharField(max_length=100)
    tprice=models.FloatField()
    disprice=models.FloatField()
    pdes=models.TextField(max_length=5000)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    pdate=models.DateField()

class order(models.Model):
    pid=models.IntegerField()
    userid=models.EmailField(max_length=100)
    remarks=models.CharField(max_length=40)
    status=models.BooleanField()
    odate=models.DateField()

class addtocart(models.Model):
    pid=models.IntegerField()
    userid=models.EmailField(max_length=100)
    status=models.BooleanField()
    cdate=models.DateField()