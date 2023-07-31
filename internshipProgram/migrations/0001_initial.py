# Generated by Django 4.2.3 on 2023-07-28 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('dob', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=150, unique=True)),
                ('qualification', models.CharField(max_length=150)),
                ('photo', models.ImageField(upload_to='imagees')),
                ('address', models.TextField()),
                ('objective', models.TextField()),
            ],
        ),
    ]