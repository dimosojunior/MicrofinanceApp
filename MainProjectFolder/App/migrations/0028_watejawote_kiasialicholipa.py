# Generated by Django 4.2.6 on 2024-11-17 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0027_watejawote_amesajiliwana'),
    ]

    operations = [
        migrations.AddField(
            model_name='watejawote',
            name='KiasiAlicholipa',
            field=models.IntegerField(blank=True, null=True, verbose_name='Kiasi Alicholipa Mpaka Sasa'),
        ),
    ]
