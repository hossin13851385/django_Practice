from django.db import models
from django.contrib.auth.models import User




class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    createt_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    

class portfolio(models.Model):
    image = models.ImageField(upload_to='prof' , default = 'default_prof.jpg' )
    status = models.BooleanField(default=False)



class skill(models.Model):
    title = models.CharField(max_length=200)
    percent = models.IntegerField(default=0) 
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title


class team(models.Model):
    image =  models.ImageField(upload_to='team' , default = 'default_team.jpg' )
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    skill = models.ManyToManyField(skill)
    descroption=models.TextField()
    status= models.BooleanField(default=True)








































# Create your models here.
