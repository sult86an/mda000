# Generated by Django 2.1.2 on 2018-11-07 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('initiatives', '0002_challenges'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(default=0)),
                ('comment', models.TextField()),
                ('report', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='initiatives.Reports')),
            ],
        ),
    ]