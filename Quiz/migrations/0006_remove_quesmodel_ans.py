# Generated by Django 4.1.3 on 2022-11-28 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0005_auto_20210512_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quesmodel',
            name='ans',
        ),
    ]
