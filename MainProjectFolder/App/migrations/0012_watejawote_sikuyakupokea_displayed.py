# Generated by Django 4.2.6 on 2024-10-08 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_watejawote_ongezaoda'),
    ]

    operations = [
        migrations.AddField(
            model_name='watejawote',
            name='SikuYaKupokea_Displayed',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Siku Ya Kupokea Bidhaa'),
        ),
    ]