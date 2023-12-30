# Generated by Django 4.2.8 on 2023-12-09 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cotegory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('type', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='batoniha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('value', models.PositiveIntegerField(default=0)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appueu.cotegory')),
            ],
        ),
        migrations.CreateModel(
            name='baton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('value', models.PositiveIntegerField(default=0)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appueu.cotegory')),
            ],
        ),
        migrations.CreateModel(
            name='basedatel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('value', models.PositiveIntegerField(default=0)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appueu.cotegory')),
            ],
        ),
    ]