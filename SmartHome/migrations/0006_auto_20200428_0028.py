# Generated by Django 3.0.5 on 2020-04-27 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartHome', '0005_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='image',
            new_name='image_small',
        ),
        migrations.AddField(
            model_name='service',
            name='image_big',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]
