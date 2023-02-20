# Generated by Django 4.1.7 on 2023-02-19 23:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('call_center_project', '0009_alter_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calllog',
            name='response',
            field=models.CharField(choices=[('Forbidden', 'Forbidden'), ('BusyHere', 'Busyhere'), ('RequestTerminated', 'Requestterminated'), ('OK', 'Ok')], max_length=100),
        ),
        migrations.AlterField(
            model_name='operatortoworkplace',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_place', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='operatortoworkplace',
            name='work_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operator', to='call_center_project.workplace'),
        ),
        migrations.AlterField(
            model_name='tenantcompany',
            name='category',
            field=models.CharField(choices=[('Unknown', 'Unknown'), ('Other', 'Other'), ('Production', 'Production'), ('Commerce', 'Commerce'), ('ServiceIndustry', 'Serviceindustry')], default='Unknown', max_length=100),
        ),
    ]
