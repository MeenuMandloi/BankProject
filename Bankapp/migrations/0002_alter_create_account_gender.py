# Generated by Django 4.0.6 on 2022-07-27 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bankapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_account',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=128),
        ),
    ]
