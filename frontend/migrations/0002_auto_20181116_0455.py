# Generated by Django 2.1.1 on 2018-11-16 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
