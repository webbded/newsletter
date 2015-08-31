from django.db import models

# Create your models here.

class SignUp(models.Model):
    email = models.EmailField(blank=False , null=True)
    fullname = models.CharField(max_length=120, blank=False, null=True)
    name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add = True , auto_now= False )
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __unicode__(self):  # for python 3.3 __str__
        return self.email
