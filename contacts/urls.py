from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('contact/delete/<int:contact_id>', views.delete_contact, name='delete_contact'),
     path('contact/edit/<int:contact_id>', views.edit_contact, name='edit_contact'),
]