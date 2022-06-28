# Generated by Django 3.2.5 on 2022-06-22 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MartMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.CharField(max_length=2)),
                ('col', models.CharField(max_length=2)),
                ('type', models.CharField(max_length=10)),
                ('junction', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'MartMap',
            },
        ),
        migrations.AddConstraint(
            model_name='martmap',
            constraint=models.UniqueConstraint(fields=('row', 'col'), name='unique MartMap'),
        ),
    ]
