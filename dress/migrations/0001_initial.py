# Generated by Django 3.2.11 on 2022-01-18 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('link', models.TextField()),
            ],
        ),
    ]
