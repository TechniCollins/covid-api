# Generated by Django 5.0 on 2023-12-27 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('state', models.CharField(max_length=100)),
                ('tcin', models.IntegerField()),
                ('tcfn', models.IntegerField()),
                ('cured', models.IntegerField()),
                ('death', models.IntegerField()),
            ],
        ),
    ]
