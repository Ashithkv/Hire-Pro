# Generated by Django 5.0.3 on 2024-08-01 20:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobopening',
            name='branch_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='candidates.location'),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='job_title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='candidates.jobtitle'),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='recruiter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='candidates.interviewer'),
        ),
    ]
