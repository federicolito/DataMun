from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lattitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SpreadSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField()),
                ('year', models.IntegerField()),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('spread_sheet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dataMun.spreadsheet')),
            ],
        ),
        migrations.CreateModel(
            name='DiagnosticCases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=32)),
                ('age', models.CharField(choices=[('<1', '<1 año'), ('1 a 5', '1 a 5 años'), ('6 a 9', '6 a 9 años'), ('10 a 14', '10 a 14 años'), ('15 a 19', '15 a 19 años'), ('20 a 54 ', '20 a 54 años'), ('55 a 64', '55 a 64 años'), ('65 y mas', '65 y mas años')], max_length=32)),
                ('cases', models.IntegerField()),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('center', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dataMun.center')),
                ('diagnostic', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dataMun.diagnostic')),
                ('week', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dataMun.week')),
            ],
        ),
        migrations.AddField(
            model_name='center',
            name='coordinate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dataMun.coordinate'),
        ),
        migrations.AddField(
            model_name='center',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataMun.zone'),
        ),
    ]
