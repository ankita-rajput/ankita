# Generated by Django 2.0.6 on 2019-09-18 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('roleId', models.AutoField(primary_key=True, serialize=False)),
                ('roleName', models.CharField(default='', max_length=200)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
    ]
