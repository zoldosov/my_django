# Generated by Django 4.1.5 on 2023-01-10 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_mentor_academy'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='academy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.academy'),
            preserve_default=False,
        ),
    ]
