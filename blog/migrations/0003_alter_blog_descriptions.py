# Generated by Django 4.0 on 2021-12-26 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_project_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='descriptions',
            field=models.TextField(),
        ),
    ]
