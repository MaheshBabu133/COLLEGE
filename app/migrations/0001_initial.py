# Generated by Django 4.1.7 on 2023-07-07 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegename', models.CharField(max_length=150)),
                ('established', models.IntegerField()),
                ('location', models.CharField(max_length=150)),
                ('website', models.URLField()),
                ('cimage', models.ImageField(upload_to=None)),
                ('branch', models.IntegerField()),
                ('course', models.CharField(max_length=100)),
                ('fees', models.IntegerField()),
            ],
        ),
    ]
