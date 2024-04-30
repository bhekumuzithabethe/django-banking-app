# Generated by Django 5.0 on 2024-04-28 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('title', models.CharField(choices=[('', 'Select'), ('Ms', 'Miss'), ('Mrs', 'Missus'), ('Mr', 'Mister'), ('Dr', 'Doctor'), ('Prof', 'Professor')], max_length=4)),
                ('sex', models.CharField(choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], max_length=15)),
                ('cellphone', models.CharField(default='+27', max_length=13)),
                ('date_of_birth', models.DateField()),
                ('identity_number', models.CharField(max_length=13)),
                ('address_line_1', models.CharField(max_length=20)),
                ('address_line_2', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=4)),
                ('province', models.CharField(choices=[('', 'Select'), ('MP', 'Mpumalanga'), ('GP', 'Gauteng'), ('NW', 'North West'), ('NC', 'Northen Cape'), ('EC', 'Eastern Cape'), ('WC', 'Western Cape'), ('FS', 'Free State'), ('LP', 'Limpopo'), ('KZN', 'Kwazulu Natal')], max_length=10)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
            ],
        ),
    ]
