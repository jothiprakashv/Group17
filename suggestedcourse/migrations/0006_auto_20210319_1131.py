# Generated by Django 2.2.10 on 2021-03-19 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suggestedcourse', '0005_auto_20210319_0955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggestedcourse',
            old_name='candiate_id',
            new_name='candidate_id',
        ),
    ]
