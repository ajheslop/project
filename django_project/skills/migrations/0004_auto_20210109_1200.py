# Generated by Django 3.1.4 on 2021-01-09 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_auto_20210109_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillsubcategory',
            name='skill_sub_category_description',
            field=models.TextField(max_length=200),
        ),
    ]
