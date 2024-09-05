# Generated by Django 5.0.1 on 2024-02-21 05:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctors", "0001_initial"),
        ("treatments", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="treatment",
            name="verified",
            field=models.CharField(
                choices=[("yes", "Yes"), ("no", "No")], max_length=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="treatment",
            name="doctor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="doctors.doctor",
            ),
        ),
    ]
