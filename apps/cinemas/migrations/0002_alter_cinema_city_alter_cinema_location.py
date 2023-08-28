# Generated by Django 4.1 on 2023-05-16 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cinemas', to='cinemas.city', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cinemas', to='cinemas.location', verbose_name='Локация'),
        ),
    ]