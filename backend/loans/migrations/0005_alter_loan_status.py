# Generated by Django 3.2.4 on 2021-06-10 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0004_alter_loan_extra_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='status',
            field=models.IntegerField(choices=[('Approved', 1), ('Rejected', 2), ('New', 3)]),
        ),
    ]
