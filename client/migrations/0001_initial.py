# Generated by Django 5.0 on 2024-04-28 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=10)),
                ('reference', models.CharField(max_length=15)),
                ('deposit_date', models.DateField(auto_now_add=True)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_account', models.CharField(max_length=10)),
                ('reference', models.CharField(max_length=15)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(max_length=10)),
                ('account_number', models.CharField(blank=True, max_length=10, null=True)),
                ('card_number', models.CharField(blank=True, max_length=16, null=True)),
                ('amount', models.FloatField()),
                ('transaction_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transfare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_account', models.CharField(max_length=10)),
                ('to_account', models.CharField(max_length=10)),
                ('reference', models.CharField(max_length=15)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=17)),
                ('card_number', models.CharField(max_length=16)),
                ('amount', models.FloatField()),
            ],
        ),
    ]
