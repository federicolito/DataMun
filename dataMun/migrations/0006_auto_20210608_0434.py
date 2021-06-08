# Generated by Django 3.2.4 on 2021-06-08 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataMun', '0005_auto_20210608_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='edad',
            field=models.CharField(choices=[('<1', '<1 año'), ('1 a 5', '1 a 5 años'), ('6 a 9', '6 a 9 años'), ('10 a 14', '10 a 14 años'), ('15 a 19', '15 a 19 años'), ('20 a 54 ', '20 a 54 años'), ('55 a  64', '55 a 64 años'), ('65 y mas', '65 y mas años')], max_length=32),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=32),
        ),
    ]
