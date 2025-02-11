# Generated by Django 2.2.6 on 2019-10-08 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190829_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='link',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
        ),
    ]
