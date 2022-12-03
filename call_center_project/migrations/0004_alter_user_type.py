# Generated by Django 4.1.3 on 2022-12-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call_center_project', '0003_alter_user_phone_number_alter_user_tenant_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('Unactive', 'Unactive'), ('Admin', 'Admin'), ('Operator', 'Operator'), ('TenantCompanyOwner', 'Tenantcompanyowner')], default='Admin', max_length=100),
        ),
    ]
