# Generated by Django 5.1.7 on 2025-03-14 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('Genre', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Director', models.CharField(max_length=100)),
                ('Year', models.IntegerField()),
                ('Music', models.CharField(max_length=100)),
            ],
        ),
    ]
