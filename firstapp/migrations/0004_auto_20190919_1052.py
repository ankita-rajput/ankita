# Generated by Django 2.0.6 on 2019-09-19 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20190919_1046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siteuser',
            old_name='useFullName',
            new_name='userFullName',
        ),
    ]