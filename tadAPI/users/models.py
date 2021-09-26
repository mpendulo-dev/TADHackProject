from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

STATUS = (
    (1,"ONLINE"),
    (0,"OFFLILE")
)

QUALIFICATION =(
     (1,"Matric"),
    (2,"Diploma"),
     (3,"Bachelor"),
    (4,"Masters")
)


class Organisation(models.Model):
    compay=models.OneToOneField(User, on_delete=CASCADE)
    profile_pic=models.ImageField(default='default.jpg', upload_to="profile_pic")
    email=models.EmailField(null=False, max_length=20)
    location= models.CharField(null=False, max_length=30)

    def __str__(self):
        return f"{self.user.username}  Profile"
    
class Learner(models.Model):
    learner=models.OneToOneField(User, on_delete=CASCADE)
    profile_pic=models.ImageField(default='default.jpg', upload_to="profile_pic")
    firstname=models.CharField(null=False, max_length=34)
    lastname=models.CharField(null=False, max_length=34)
    username=models.CharField(null=False, max_length=34)
    email=models.EmailField(null=False, max_length=34)
    coins=models.IntegerField(default=0)
    address=models.CharField(null=False, max_length=34)


class Tutor(models.Model):
    tutor=models.OneToOneField(User, on_delete=CASCADE)
    profile_pic=models.ImageField(default='default.jpg', upload_to="profile_pic")
    firstname=models.CharField(null=False, max_length=34)
    lastname=models.CharField(null=False, max_length=34)
    username=models.CharField(null=False, max_length=34)
    email=models.EmailField(null=False, max_length=34)
    address=models.CharField(null=False, max_length=34)
    high_qualification= models.IntegerField(choices=QUALIFICATION , default=1)
    ID_Document=  models.FileField(upload_to='documents/', null=True)
    qualification = models.FileField(upload_to='documents/', null=True)
    proof_of_residence=  models.FileField(upload_to='documents/', null=True)
    specialization=models.CharField(null=False, max_length=30)

   

# Create your models here.
