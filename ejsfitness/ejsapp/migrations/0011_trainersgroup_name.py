# Generated by Django 4.2.4 on 2024-08-12 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejsapp', '0010_trainersgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainersgroup',
            name='name',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
