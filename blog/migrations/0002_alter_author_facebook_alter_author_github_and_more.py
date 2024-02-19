# Generated by Django 5.0.2 on 2024-02-19 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='facebook',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='github',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='instagram',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='twitter',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='comments',
            name='image',
            field=models.ImageField(upload_to='comments'),
        ),
        migrations.AlterField(
            model_name='instagram',
            name='image',
            field=models.ImageField(upload_to='insta'),
        ),
    ]
