# Generated by Django 4.0.3 on 2022-04-05 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_file_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='pdf',
            field=models.FileField(upload_to='sketchdb/pdfs'),
        ),
    ]