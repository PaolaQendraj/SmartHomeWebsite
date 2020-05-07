# Generated by Django 3.0.5 on 2020-04-28 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartHome', '0012_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]