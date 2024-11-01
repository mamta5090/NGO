from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.

def index(request):
    data=slider.objects.all().order_by('-id')[0:2]
    bdata=myblog.objects.all().order_by('-id')[0:6]
    im = igallery.objects.all().order_by('-id')
    mydict={"res":data,"data":bdata,"img":im}
    return render(request,'user/index.html',mydict)

#############################################
def about(request):

    return render(request,'user/about.html')
#############################################

def contact(request):
    status=False
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mob')
        message=request.POST.get('msg')
        contactus(Name=name,Email=email,Mobile=mobile,Message=message).save()
        status=True

    return render(request,'user/contact.html',context={"msg":status})

#############################################

def video(request):
    data=vgallery.objects.all().order_by('-id')
    myd={"vdata":data}
    return render(request,'user/video.html',myd)
##############################################

def vdodetails(request):
    y=request.GET.get('msg')
    x=vgallery.objects.all().filter(id=y)
    myd={"vdata":x}
    return render(request,'user/details.html',myd)

#############################################

def gallery(request):
    d=igallery.objects.all().order_by('-id')
    mydict={"data":d}
    return render(request,'user/gallery.html',context=mydict)

#############################################
def blog(request):
    bdata=myblog.objects.all().order_by('-id')
    if request.method=="POST":
        s=request.POST.get('search')
        if s is not "":
            bdata=myblog.objects.all().filter(Q(bname__icontains=s) | Q(bdes__icontains=s))
        else:
            return HttpResponse("<script>alert('Please Enter Data for Search');location.href='/user/blog/'</script>")


    mydict={"bdata":bdata}
    return render(request,'user/blog.html',mydict)

#############################################
def ndetails(request):
    return render(request,'user/ndetails.html')

#############################################
def donate(request):
    countries=country.objects.all().order_by('-id')
    states=state.objects.all().order_by('-id')
    if request.method=="POST":
        ammount=request.POST.get('ammt')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        mob=request.POST.get('mob')
        count=request.POST.get('country')
        address=request.POST.get('address')
        stat=request.POST.get('state')
        pcode=request.POST.get('pcode')
        occn=request.POST.get('occn')
        donates(ammt=ammount,fname=fname,lname=lname,email=email,mob=mob,country=count,address=address,state=stat,pcode=pcode,occn=occn).save()
    return render(request,'user/donate.html',context={"cnt":countries,"st":states})

#############################################

def membership(request):
    cities=city.objects.all().order_by('-id')
    if request.method=="POST":
        name=request.POST.get('name')
        pcode=request.POST.get('pcode')
        c=request.POST.get('city')
        email=request.POST.get('email')
        mob=request.POST.get('mob')
        acc=request.POST.get('acc')
        padd=request.POST.get('paddress')
        cadd=request.POST.get('caddress')
        pic=request.FILES.get('ppic')
        members(name=name,pcode=pcode,city=c,email=email,mob=mob,acc=acc,paddress=padd,caddress=cadd,ppic=pic).save()
    return render(request,'user/membership.html',context={"ct":cities})

#############################################

#def login(request):
#    return render(request,'user/login.html')

##################################################
def causes(request):
    return render(request,'user/causes.html')
###################################################
def blogdetail(request):
    a=request.GET.get('msg')
    d=myblog.objects.all().filter(id=a)
    md={"data":d}
    return  render(request,'user/bdetail.html',md)




