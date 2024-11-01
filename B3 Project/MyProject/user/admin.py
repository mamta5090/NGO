from django.contrib import admin
from .models import *

# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display = ("Name","Email","Mobile","Message")

admin.site.register(contactus,contactusAdmin)
######################################################

class igalleryAdmin(admin.ModelAdmin):
    list_display = ('id','gname','gpic')

admin.site.register(igallery,igalleryAdmin)
#################################################################

class sliderAdmin(admin.ModelAdmin):
    list_display = ('id','shead','ssubject','sdes','spic')

admin.site.register(slider,sliderAdmin)
#################################################################
class myblogAdmin(admin.ModelAdmin):
    list_display = ('id','bname','bdes','bpicture','bdate')
admin.site.register(myblog,myblogAdmin)
#################################################################
class ncategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category','cpic','cdate')
admin.site.register(ncategory,ncategoryAdmin)
################################################################
class cityAdmin(admin.ModelAdmin):
    list_display = ('id','ncity','cdate')
admin.site.register(city,cityAdmin)
###############################################################
class membersAdmin(admin.ModelAdmin):
    list_display=('id','name','email','acc','caddress','paddress','ppic','mob','pcode','city')
admin.site.register(members,membersAdmin)
###############################################################
class countryAdmin(admin.ModelAdmin):
    list_display = ('id','ncountry','cdate')
admin.site.register(country,countryAdmin)
##############################################################
class stateAdmin(admin.ModelAdmin):
    list_display = ('id','nstate','sdate')
admin.site.register(state,stateAdmin)
###############################################################
class donatesAdmin(admin.ModelAdmin):
    list_display = ('id','ammt','fname','lname','email','mob','country','address','state','pcode','occn')
admin.site.register(donates,donatesAdmin)
#####################################################################
class vgalleryAdmin(admin.ModelAdmin):
    list_display=('id','vlink','vdes','vdate')
admin.site.register(vgallery,vgalleryAdmin)
