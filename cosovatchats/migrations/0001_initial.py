# Generated by Django 2.0.1 on 2018-01-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cosovatchat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('matruong', models.CharField(blank=True, default='', max_length=10)),
                ('skytuc', models.FloatField()),
                ('sokytuc', models.FloatField()),
                ('sphonghoc', models.FloatField()),
                ('sthuvien', models.FloatField()),
                ('svandong', models.FloatField()),
                ('tongdientich', models.FloatField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
