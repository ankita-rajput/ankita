from django.db import models


class UserRole(models.Model):
    roleId=models.AutoField(primary_key=True)
    roleName=models.CharField(max_length=200,default="", null=True)
    isActive=models.NullBooleanField(default=True)


class SiteUser(models.Model):
    roleId=models.ForeignKey(UserRole,on_delete=models.CASCADE)
    userFullName=models.CharField(max_length=200,default="", null=True)
    userEmail=models.CharField(primary_key=True,max_length=200,default="")
    userPassword=models.CharField(max_length=200,default="")
    userMobile=models.BigIntegerField()
    isActive=models.BooleanField(default=True)

class Image(models.Model):
    roleId = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    userFullName = models.CharField(max_length=200, default="", null=True)
    userEmail = models.CharField(primary_key=True, max_length=200, default="")
    userPassword = models.CharField(max_length=200, default="")
    userMobile = models.BigIntegerField()
    userImage=models.CharField(max_length=200, default="",null=True)
    isActive = models.BooleanField(default=True)


