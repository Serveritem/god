# Generated by Django 4.2.4 on 2024-08-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejsapp', '0007_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='main')),
            ],
        ),
    ]
