from django.shortcuts import render,redirect, get_object_or_404
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from contacts.forms import ContactForm
# Create your views here.
def contact(request):
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        listing = request.POST["listing"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        realtor_email = request.POST["realtor_email"]
        user_id = request.POST["user_id"]
        if request.user.is_authenticated:
            has_contacted = Contact.objects.filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,"You have already made an inquiry for this listing")
                return redirect('listings:listing',listing_id=listing_id)
        contact = Contact(listing=listing,listing_id=listing_id,name=name,
                          email=email,phone=phone,message=message, user_id=user_id)
        contact.save()
        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
        #     'Ryanlai@gmail.com', # admin email 
        #     [realtor_email],   # realtor email
        #     fail_silently=False
        # )
        messages.success(request,"Your request has been submitted, a realtor will get back to you soon")
        return redirect('listings:listing',listing_id=listing_id)

def delete_contact(request,contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    return redirect("accounts:dashboard")

def edit_contact(request,contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == "POST":
        form = ContactForm(request.POST,instance=contact)
        if form.is_valid():
            form.save()
            return redirect("accounts:dashboard")
    else:
        form = ContactForm(instance=contact)    
        
    return render(request,"contacts/edit_message.html",{"form":form})