from django.contrib import admin
from . models import Listing, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug':('name',)}

class ListingAdmin(admin.ModelAdmin):
    list_display = ('company_name','user','category','email','phone_number','country','logo')
    prepopulated_fields = {'slug':('company_name',)}
    list_editable = ('logo',)

admin.site.register(Listing,ListingAdmin)
admin.site.register(Category,CategoryAdmin)
