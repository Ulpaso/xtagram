# Generated by Django 4.2.3 on 2024-08-13 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_user_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tags',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]