# Generated by Django 5.0.3 on 2024-03-20 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thum',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
