# Generated by Django 2.2.10 on 2021-03-18 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestedcourse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestedcourse',
            name='mentee_id',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='suggestedcourse',
            name='mentee_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
