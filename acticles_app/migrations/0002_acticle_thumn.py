# Generated by Django 4.2 on 2023-04-06 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acticles_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acticle',
            name='thumn',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
