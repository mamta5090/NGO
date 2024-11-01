from django.db import models

# Create your models here.
class contactus(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=40)
    Mobile=models.CharField(max_length=30)
    Message=models.TextField()
def __str__(self):
    return self.Name

class slider(models.Model):
    shead=models.CharField(max_length=300)
    ssubject=models.CharField(max_length=500)
    sdes=models.TextField()
    spic=models.ImageField(upload_to='static/slider/',default="")
    def __str__(self):
        return self.shead
############################################################
class igallery(models.Model):
    gname=models.CharField(max_length=400)
    gpic=models.ImageField(upload_to='static/gallery/',default="")


############################################################
class myblog(models.Model):
    bname=models.CharField(max_length=40)
    bdes=models.TextField()
    bpicture=models.ImageField(upload_to='static/blogs',null=True)
    bdate=models.DateField()
############################################################
class ncategory(models.Model):
    category=models.CharField(max_length=80)
    cpic=models.ImageField(upload_to='static/category',null=True)
    cdate=models.DateField()
############################################################
class city(models.Model):
    ncity=models.CharField(max_length=30)
    cdate=models.DateField()
###########################################################
class members(models.Model):
    name=models.CharField(max_length=90)
    pcode=models.TextField(max_length=10)
    city=models.CharField(max_length=100)
    email=models.CharField(max_length=90)
    mob=models.CharField(max_length=30)
    acc=models.CharField(max_length=30)
    caddress=models.TextField()
    paddress=models.TextField()
    ppic=models.ImageField(upload_to='static/profile/',null=True)

def __str__(self):
    return self.Name
#######################################################################

class country(models.Model):
    ncountry=models.CharField(max_length=30)
    cdate=models.DateField()

#######################################################################

class state(models.Model):
    nstate=models.CharField(max_length=30)
    sdate=models.DateField()

#######################################################################
class donates(models.Model):
    ammt=models.TextField(max_length=28)
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    mob=models.TextField(max_length=30)
    country=models.CharField(max_length=30)
    address=models.CharField(max_length=80)
    state=models.CharField(max_length=30)
    pcode=models.TextField(max_length=30)
    occn=models.CharField(max_length=100)
    payss=models.ImageField(upload_to='static/payment',null=True)
def __str__(self):
    return self.name
#############################################################################
class vgallery(models.Model):
    vlink=models.TextField()
    vdes=models.TextField()
    vtitle=models.CharField(max_length=200)
    vdate=models.DateField()