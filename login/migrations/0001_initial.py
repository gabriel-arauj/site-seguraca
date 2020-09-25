# Generated by Django 3.1.1 on 2020-09-24 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_inseguro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255, verbose_name='Usuário')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
            ],
            options={
                'verbose_name': 'Usuário Inseguro',
                'verbose_name_plural': 'Usuários Inseguros',
            },
        ),
    ]
