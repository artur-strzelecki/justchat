# Generated by Django 3.1.7 on 2021-03-01 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justchatapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicmessage',
            name='author',
            field=models.TextField(),
        ),
    ]