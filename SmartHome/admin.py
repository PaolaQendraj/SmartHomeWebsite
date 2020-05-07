from django.contrib import admin
from .models import Header, About, Features, Inovation, Service, Service_Info, Other_Service, Footer, \
    Contact_Content, Contact, Subscription, Side_Menu

# Register your models here.
admin.site.register(Header)
admin.site.register(About)
admin.site.register(Features)
admin.site.register(Inovation)
admin.site.register(Service)
admin.site.register(Service_Info)
admin.site.register(Other_Service)
admin.site.register(Footer)
admin.site.register(Contact_Content)
admin.site.register(Contact)
admin.site.register(Subscription)
admin.site.register(Side_Menu)