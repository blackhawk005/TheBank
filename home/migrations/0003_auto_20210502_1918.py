# Generated by Django 3.1.5 on 2021-05-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_transfers_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.CharField(max_length=200)),
                ('recieved', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Transfers',
        ),
    ]