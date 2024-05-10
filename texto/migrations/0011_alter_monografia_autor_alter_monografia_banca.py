# Generated by Django 5.0.4 on 2024-05-10 21:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipe', '0001_initial'),
        ('texto', '0010_alter_monografia_nota_final'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monografia',
            name='autor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='autor_monografias', to='equipe.pesquisador'),
        ),
        migrations.AlterField(
            model_name='monografia',
            name='banca',
            field=models.ManyToManyField(blank=True, limit_choices_to={'cargo': 'TECNICO'}, null=True, to='equipe.pesquisador', verbose_name='banca'),
        ),
    ]
