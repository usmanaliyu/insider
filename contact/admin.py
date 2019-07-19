from django.contrib import admin
from . models import Contact,Subscribe

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message')




admin.site.register(Contact, ContactAdmin)
admin.site.register(Subscribe)
