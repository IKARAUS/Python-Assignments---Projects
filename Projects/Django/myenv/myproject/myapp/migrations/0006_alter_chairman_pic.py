# Generated by Django 3.2.13 on 2022-07-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_chairman_about_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairman',
            name='pic',
            field=models.FileField(default='media/default_chairman.png', upload_to='images/'),
        ),
    ]
