# Generated by Django 2.2.5 on 2019-10-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='voto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partido', models.TextField()),
                ('color', models.TextField()),
                ('votos', models.IntegerField()),
            ],
        ),
    ]
