# Generated by Django 4.2.4 on 2024-08-22 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejsapp', '0013_head'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250)),
                ('name2', models.CharField(max_length=250)),
                ('name3', models.CharField(max_length=250)),
                ('description1', models.TextField(max_length=250)),
                ('description2', models.TextField(max_length=250)),
                ('description3', models.TextField(max_length=250)),
            ],
        ),
    ]
