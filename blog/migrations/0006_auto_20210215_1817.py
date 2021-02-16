# Generated by Django 3.1.6 on 2021-02-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210215_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='excerpt',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(max_length=220),
        ),
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
