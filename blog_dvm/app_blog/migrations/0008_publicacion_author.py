# Generated by Django 4.0.3 on 2022-03-29 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0007_alter_publicacion_date_of_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='author',
            field=models.CharField(default='Missing author', max_length=40),
        ),
    ]
