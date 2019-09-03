# Generated by Django 2.1.2 on 2019-09-02 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('maxstudent', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=100)),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapp.Student'),
        ),
    ]
