# Generated by Django 4.0.6 on 2022-07-10 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
    ]
