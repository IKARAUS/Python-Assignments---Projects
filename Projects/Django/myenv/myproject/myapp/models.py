from pickle import TRUE
from pyexpat import model
from django.db import models

# Create your models here.

class user(models.Model):
    email = models.EmailField(unique= True,max_length=50)
    password = models.CharField(max_length = 30)
    otp = models.IntegerField(default = 459)
    role = models.CharField(max_length = 10)
    is_active = models.BooleanField(default=False)
    is_verfied = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)


    def __str__(self)-> str:
        return self.email

class chairman(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=30)
    contect=models.CharField(max_length=15)
    block_no=models.CharField(max_length=10,null=True)
    house_no=models.CharField(max_length=10,null=True)
    about_me=models.TextField(max_length=50,null=True)
    pic=models.FileField(upload_to='images/',default='media/default_chairman.png')

    def __str__(self)-> str:
        return self.firstname +" "+ self.lastname


class notice(models.Model):
    user_id=models.ForeignKey(chairman,on_delete=models.CASCADE)
    notice_title=models.CharField(max_length=85)
    notice_content=models.TextField(max_length=85)
    img=models.ImageField(upload_to='images/Notice')
    video=models.FileField(upload_to='images/Notice/videos')

    def __str__(self):
        return self.notice_title