# Generated by Django 4.0.3 on 2022-03-29 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='apellido',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='lugar_de_trabajo',
            new_name='occupation',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='ocupacion',
            new_name='workplace',
        ),
    ]