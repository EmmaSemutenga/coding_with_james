# Generated by Django 3.2.6 on 2021-09-06 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papersdb', '0004_auto_20210906_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='keyword',
            field=models.CharField(choices=[('ed-tech', 'ed-tech'), ('novel', 'novel'), ('sci-fi', 'sci-fi')], default='ed-tech', max_length=20),
        ),
    ]
