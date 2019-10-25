# Generated by Django 2.1.12 on 2019-10-19 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=255)),
                ('To', models.CharField(max_length=255)),
                ('typeofdel', models.CharField(choices=[('paper', 'paper'), ('parcel', 'parcel')], max_length=255)),
                ('Postal_rate', models.CharField(choices=[('10', '10'), ('20', '20')], max_length=255)),
                ('weightrate', models.CharField(choices=[('10', '10'), ('20', '20')], max_length=255)),
                ('del_pin_no', models.IntegerField(max_length=255)),
                ('Describe_del', models.CharField(max_length=255)),
                ('Full_area_address', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
