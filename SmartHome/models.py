from django.db import models

# Create your models here.

class Header(models.Model):
    line_one = models.CharField(max_length=50)
    line_two = models.CharField(max_length=100)
    line_three = models.CharField(max_length=100)
    line_four = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.line_one

class About(models.Model):
    line_one = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.line_one


class Features(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Inovation(models.Model):
    line_one = models.CharField(max_length=50)
    line_two = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.line_one


class Service(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200)
    long_description = models.CharField(max_length=2000)
    image_small = models.ImageField(upload_to='media')
    image_big = models.ImageField(upload_to='media', default='')

    def __str__(self):
        return self.name

class Service_Info(models.Model):
    service_name = models.CharField(max_length=50, default='')
    info = models.CharField(max_length=500)

    def __str__(self):
        return self.service_name

class Other_Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Footer(models.Model):
    logo = models.ImageField(upload_to='media')
    image = models.ImageField(upload_to='media')
    description = models.CharField(max_length=200)
    link_facebook = models.CharField(max_length=200)
    link_instagram = models.CharField(max_length=200)
    adress = models.CharField(max_length=100)
    tel_one = models.CharField(max_length=50)
    tel_two = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    copyright_text = models.CharField(max_length=50)

class Contact_Content(models.Model):
    header_one = models.CharField(max_length=50)
    line_one = models.CharField(max_length=200)
    header_two = models.CharField(max_length=50)
    line_two = models.CharField(max_length=200)
    iframe = models.CharField(max_length=3000)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=3000)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.email

class Side_Menu(models.Model):
    text = models.CharField(max_length=500)






