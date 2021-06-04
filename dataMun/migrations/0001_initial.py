# Generated by Django 3.2.4 on 2021-06-04 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(default=0)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Semana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semana', models.IntegerField()),
                ('year', models.IntegerField()),
                ('creacion', models.DateTimeField(blank=True)),
                ('tabla', models.FileField(null=True, upload_to='data/')),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=32)),
                ('edad', models.CharField(choices=[('1', '1'), ('1 / 5', '1 a 5'), ('6 / 9', '6 a 9'), ('10 / 14', '10 a 14'), ('15 / 19', '15 a 19'), ('20 / 54 ', '20 a 54 '), ('55 /  64', '55 a  64'), ('65+', '65 y mas')], max_length=32)),
                ('creacion', models.DateTimeField(blank=True)),
                ('centro', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dataMun.centro')),
                ('diagnostico', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dataMun.diagnostico')),
                ('semana', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dataMun.semana')),
            ],
        ),
        migrations.AddField(
            model_name='centro',
            name='zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataMun.zona'),
        ),
    ]