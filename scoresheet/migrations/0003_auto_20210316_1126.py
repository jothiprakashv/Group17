# Generated by Django 2.2.10 on 2021-03-16 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoresheet', '0002_filestoreage'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoresheet',
            name='candidate_id',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scoresheet',
            name='gender',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
