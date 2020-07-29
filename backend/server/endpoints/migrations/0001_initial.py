# Generated by Django 2.2.4 on 2020-07-06 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Symptoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=256)),
                ('lastname', models.CharField(max_length=256)),
                ('symptoms', models.CharField(choices=[('itching', 'itching'), ('skin_rash', 'skin_rash'), ('nodal_skin_eruptions', 'nodal_skin_eruptions'), ('continuous_sneezing', 'continuous_sneezing'), ('shivering', 'shivering')], max_length=256)),
            ],
        ),
    ]
