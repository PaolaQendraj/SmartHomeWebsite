from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Header, About, Features, Inovation, Service, Service_Info, Other_Service, Footer, \
    Contact_Content, Contact, Subscription, Side_Menu
# Create your views here.
def index(request):
    if request.method == 'GET':
        header = Header.objects.all()
        header1 = header[0]
        about = About.objects.all()
        about1 = about[0]
        features = Features.objects.all()
        features1 = features[0]
        features2 = features[1]
        features3 = features[2]
        inovation = Inovation.objects.all()
        inovation1 = inovation[0]
        service = Service.objects.all()
        footer = Footer.objects.all()
        footer1 = footer[0]
        side_menu = Side_Menu.objects.all()
        side_menu1 = side_menu[0]
        context = {'header1': header1, 'about1': about1, 'features1': features1, 'features2': features2, 'features3':
            features3, 'inovation1': inovation1, 'service': service, 'footer1': footer1, 'side_menu1': side_menu1}
        return render(request, 'index.html', context)

def services(request):
    if request.method == 'GET':
        service = Service.objects.all()
        service_info = Service_Info.objects.all()
        other_services = Other_Service.objects.all()
        footer = Footer.objects.all()
        footer1 = footer[0]
        side_menu = Side_Menu.objects.all()
        side_menu1 = side_menu[0]
        context = {'service': service, 'other_services': other_services, 'service_info': service_info, 'footer1':
            footer1, 'side_menu1': side_menu1}
        return render(request, 'services.html', context)

def contact(request):
    if request.method == 'GET':
        content = Contact_Content.objects.all()
        content1 = content[0]
        footer = Footer.objects.all()
        footer1 = footer[0]
        side_menu = Side_Menu.objects.all()
        side_menu1 = side_menu[0]
        context = {'content1': content1, 'footer1': footer1,'side_menu1': side_menu1}
        return render(request, 'contact.html', context)
    elif request.method == 'POST':
        contactus = request.POST
        name = contactus['name']
        email = contactus['email']
        subject = contactus['subject']
        message = contactus['message']
        InsertContact=Contact(name=name, email=email, subject=subject, message=message)
        InsertContact.save()
        content = Contact_Content.objects.all()
        content1 = content[0]
        footer = Footer.objects.all()
        footer1 = footer[0]
        side_menu = Side_Menu.objects.all()
        side_menu1 = side_menu[0]
        context = {'content1': content1, 'footer1': footer1, 'side_menu1': side_menu1}
        return render(request, 'contact.html', context)

def subscribe(request):
    if request.method == 'POST':
        subscriber = request.POST
        email = subscriber['email']
        InsertSubscriber=Subscription(email=email)
        InsertSubscriber.save()
        return HttpResponseRedirect('/')
