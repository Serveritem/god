# Generated by Django 4.2.4 on 2024-08-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejsapp', '0008_mainphotos'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainphotos',
            name='name',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
