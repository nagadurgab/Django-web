from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    designation=models.CharField(max_length=20,null=False,blank=False)
    salary=models.IntegerField(null=True,blank=True)
    class Meta:
        ordering=('-salary',)

def __str__(slef):
    return "{0} {1}".format(self.User.first_name,self.User.last_name)
