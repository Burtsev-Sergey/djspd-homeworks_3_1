# Generated by Django 4.2.7 on 2025-03-25 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='mark',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Satisfactory'), (4, 'Good'), (5, 'Perfect')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='main.product'),
        ),
    ]
