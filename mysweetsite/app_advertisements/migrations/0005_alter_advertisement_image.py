# Generated by Django 3.2.20 on 2023-08-12 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0004_advertisement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(upload_to='advertisements/', verbose_name='изображение'),
        ),
    ]