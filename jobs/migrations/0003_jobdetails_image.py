# Generated by Django 2.0.2 on 2018-03-29 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_remove_jobdetails_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetails',
            name='image',
            field=models.ImageField(default='SOME STRING', upload_to='images/'),
        ),
    ]