# Generated by Django 5.0.7 on 2024-08-02 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='codigoEstudiante',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
