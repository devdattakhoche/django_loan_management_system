# Generated by Django 3.2.4 on 2021-06-10 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0005_alter_loan_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='status',
            field=models.IntegerField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('New', 'New')]),
        ),
    ]
