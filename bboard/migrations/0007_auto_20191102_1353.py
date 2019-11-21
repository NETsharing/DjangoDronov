# Generated by Django 2.2.5 on 2019-11-02 10:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0006_auto_20191023_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='title',
            field=models.CharField(error_messages={'invalid': 'Направильное название товара'}, max_length=50, unique=True, validators=[django.core.validators.RegexValidator(regex='^.{4,}$')], verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='TypeModeration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.ManyToManyField(null=True, to='bboard.Moderator', verbose_name='Тип модераций')),
            ],
        ),
    ]
