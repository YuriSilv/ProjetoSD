# Generated by Django 5.0.4 on 2024-04-24 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipe', '0001_initial'),
        ('texto', '0004_monografia_area_concentração_monografia_autor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='monografia',
            name='banca',
            field=models.ManyToManyField(blank=True, null=True, to='equipe.pesquisador'),
        ),
    ]
