# Generated by Django 3.2.6 on 2021-11-19 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='desc',
            field=models.TextField(default=-1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='img',
            field=models.ImageField(default=1.0, upload_to='image'),
            preserve_default=False,
        ),
    ]
