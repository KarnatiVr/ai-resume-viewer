# Generated by Django 5.0.3 on 2024-03-11 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeViewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='feedback',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]