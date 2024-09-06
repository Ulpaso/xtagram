# Generated by Django 4.2.3 on 2024-05-01 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_descripcion_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='Nuevo post', max_length=50),
        ),
    ]