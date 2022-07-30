# Generated by Django 4.0.6 on 2022-07-24 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('spec', models.CharField(max_length=120)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]