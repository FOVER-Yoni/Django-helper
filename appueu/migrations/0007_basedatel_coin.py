# Generated by Django 4.2.8 on 2023-12-09 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appueu', '0006_remove_basedatel_coin'),
    ]

    operations = [
        migrations.AddField(
            model_name='basedatel',
            name='coin',
            field=models.PositiveIntegerField(default=0),
        ),
    ]