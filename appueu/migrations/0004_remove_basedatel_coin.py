# Generated by Django 4.2.8 on 2023-12-09 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appueu', '0003_basedatel_coin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basedatel',
            name='coin',
        ),
    ]
