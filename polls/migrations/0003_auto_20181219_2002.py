# Generated by Django 2.1.4 on 2018-12-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20181219_1939'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200),
        ),
    ]
