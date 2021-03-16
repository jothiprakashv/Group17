# Generated by Django 2.2.10 on 2021-03-12 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(default='', max_length=20)),
                ('course_name', models.CharField(max_length=30)),
                ('attempt_id', models.CharField(max_length=30)),
                ('candidate_name', models.CharField(max_length=30)),
                ('candidate_email', models.EmailField(blank=True, max_length=254)),
                ('mark', models.IntegerField()),
                ('grade', models.CharField(max_length=30)),
            ],
        ),
    ]