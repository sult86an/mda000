# Generated by Django 2.1.2 on 2018-11-08 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiatives', '0004_auto_20181108_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='risks',
            name='plan',
            field=models.TextField(),
        ),
    ]
