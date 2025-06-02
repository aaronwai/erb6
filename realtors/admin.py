from django.contrib import admin

from .models import Realtor
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'is_mvp')
    list_display_links = ('id', 'name')
    list_editable = 'is_mvp', 'email', 'phone' 
    search_fields = ('name',)
    list_per_page = 25   


admin.site.register(Realtor, RealtorAdmin)