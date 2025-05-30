from django.contrib import admin

# Register your models here.
from .models import Listing
from django.forms import NumberInput
from django.db import models
class ListingAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'is_published', 'price', 'list_date', 'realtor'
    list_display_links = 'id', 'title'
    list_filter = 'realtor',
    list_editable = 'is_published', 'price'
    search_fields = 'title', 'description', 'address', 'price'
    list_per_page = 25
    ordering = ['-id']
    #prepopulated_fields = {'title': ('title',)}
    formfield_overrides = {
        models.IntegerField: {'widget': NumberInput(attrs= {'size': '10'})}}
    show_facets = admin.ShowFacets.ALWAYS
admin.site.register(Listing, ListingAdmin)