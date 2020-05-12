# Generated by Django 3.0.5 on 2020-05-11 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200506_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entreprise',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Adresse email'),
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='link',
            field=models.URLField(blank=True, default='https://', verbose_name='Site internet'),
        ),
    ]