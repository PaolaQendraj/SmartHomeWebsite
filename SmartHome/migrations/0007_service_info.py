# Generated by Django 3.0.5 on 2020-04-27 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SmartHome', '0006_auto_20200428_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=500)),
                ('service', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='SmartHome.Service')),
            ],
        ),
    ]
