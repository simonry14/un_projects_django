# Generated by Django 3.2.12 on 2022-02-04 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20220204_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='approval_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.approval_status'),
        ),
        migrations.AddField(
            model_name='project',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.country'),
        ),
        migrations.AddField(
            model_name='project',
            name='donor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.donor'),
        ),
        migrations.AddField(
            model_name='project',
            name='fund',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.fund'),
        ),
        migrations.AddField(
            model_name='project',
            name='lead_org_unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.lead_org_unit'),
        ),
        migrations.AddField(
            model_name='project',
            name='paas_code',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.paas_code'),
        ),
        migrations.AddField(
            model_name='project',
            name='theme',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.theme'),
        ),
    ]
