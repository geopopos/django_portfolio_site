# Generated by Django 2.2.5 on 2019-09-29 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20190929_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
