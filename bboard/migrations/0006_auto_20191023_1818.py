# Generated by Django 2.2.5 on 2019-10-23 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0005_auto_20191023_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moderator',
            name='name',
        ),
        migrations.AddField(
            model_name='bb',
            name='moderator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.Moderator'),
        ),
        migrations.AddField(
            model_name='moderator',
            name='nameMod',
            field=models.CharField(max_length=20, null=True, verbose_name='Модератор'),
        ),
        migrations.DeleteModel(
            name='TypeModeration',
        ),
    ]
