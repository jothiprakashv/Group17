# Generated by Django 2.2.10 on 2021-03-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestedcourse', '0007_suggestedcourse_assigned_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestedcourse',
            name='status',
            field=models.CharField(default='Assigned', max_length=30),
        ),
    ]