# Generated by Django 2.1.7 on 2019-03-23 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='url',
            field=models.URLField(default='#'),
            preserve_default=False,
        ),
    ]
