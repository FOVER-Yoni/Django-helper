# Generated by Django 4.2.8 on 2023-12-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='coin',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
