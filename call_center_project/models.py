from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CheckConstraint, Q


class GenderType(models.TextChoices):
    Unknown = 'Unknown'
    Other = 'Other'
    Male = 'Male'
    Female = 'Female'


class AccountType(models.TextChoices):
    Admin = 'Admin'
    Operator = 'Operator'
    TenantCompanyOwner = 'TenantCompanyOwner'


class CategoryType(models.TextChoices):
    Unknown = 'Unknown'
    Other = 'Other'
    Production = 'Production'
    Commerce = 'Commerce'
    ServiceIndustry = 'ServiceIndustry'


class DisconnectInitiatorType(models.TextChoices):
    Origination = 'Origination'
    Operator = 'Destination'


class ResponseType(models.TextChoices):
    Forbidden = 'Forbidden'
    BusyHere = 'BusyHere'
    RequestTerminated = 'RequestTerminated'
    OK = 'OK'


class Address(models.Model):
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    building = models.CharField(max_length=100, blank=True)
    additional_info = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.id}| {self.country}"


class Office(models.Model):
    address = models.ForeignKey(
        'call_center_project.Address', models.SET_NULL, related_name='offices', null=True, blank=True)
    title = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'address', 'title'
                ],
                name='unique_office')
        ]


class Software(models.Model):
    title = models.CharField(max_length=100, unique=True)


class SoftwareVersion(models.Model):
    version = models.CharField(max_length=100)
    software = models.ForeignKey('call_center_project.Software',
                                 on_delete=models.CASCADE, related_name='software_versions')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'version', 'software'
                ],
                name='unique_software_version')
        ]


class WorkPlace(models.Model):
    room_number = models.CharField(max_length=100)
    office = models.ForeignKey(
        'call_center_project.Office', models.CASCADE, related_name='work_places')
    software_version = models.ForeignKey(
        'call_center_project.SoftwareVersion', models.SET_NULL, related_name='work_places', null=True, blank=True)
    tenant_company = models.ForeignKey(
        'call_center_project.TenantCompany', models.SET_NULL, related_name='work_places', null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'room_number', 'office'
                ],
                name='unique_work_place')
        ]


class TenantCompany(models.Model):
    isdisabled = models.BooleanField(default=False)
    title = models.CharField(max_length=100, unique=True)
    category = models.CharField(
        max_length=100, choices=CategoryType.choices, default=CategoryType.Unknown)
    price_per_operator = models.FloatField(blank=True)

    class Meta:
        constraints = (
            # for checking in the DB
            CheckConstraint(
                check=Q(price_per_operator__gte=0.0),
                name='tenant_company_price_per_operator_range'),
        )


class TenantCompanyPhoneNumber(models.Model):
    phone_number = models.CharField(max_length=100, unique=True),
    tenant_company = models.ForeignKey(
        'call_center_project.TenantCompany', models.CASCADE, related_name='tenant_company_phone_numbers')
    description = models.TextField(blank=True)


class CallerPerson(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, unique=True)
    gender = models.CharField(
        max_length=100, choices=GenderType.choices, default=GenderType.Unknown)
    email = models.EmailField(blank=True, null=True, default=None)


class User(AbstractUser):
    type = models.CharField(
        max_length=100, choices=AccountType.choices, default=AccountType.Admin)
    isdisabled = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    gender = models.CharField(
        max_length=100, choices=GenderType.choices, default=GenderType.Unknown)
    phone_number = models.CharField(max_length=100, null=True, default=None)
    tenant_company = models.ForeignKey(
        'call_center_project.TenantCompany', models.SET_NULL, related_name='users', null=True)


class OperatorToWorkPlace(models.Model):
    operator = models.ForeignKey(
        'call_center_project.User', models.CASCADE, related_name='work_places')
    work_place = models.ForeignKey(
        'call_center_project.WorkPlace', models.CASCADE, related_name='operators')


class CallLog(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveSmallIntegerField()
    caller_person = models.ForeignKey(
        'call_center_project.CallerPerson', models.CASCADE, related_name='call_logs')
    caller_person_message = models.TextField(blank=True)
    tenant_company_phone_number = models.ForeignKey(
        'call_center_project.TenantCompanyPhoneNumber', models.CASCADE, related_name='call_logs')
    operator = models.ForeignKey(
        'call_center_project.User', models.SET_NULL, related_name='call_logs', null=True)
    operator_message = models.TextField(blank=True)
    disconnect_initiator = models.CharField(
        max_length=100, choices=DisconnectInitiatorType.choices)
    response = models.CharField(max_length=100, choices=ResponseType.choices)
    paid = models.FloatField()
    address = models.ForeignKey(
        'call_center_project.Address', models.SET_NULL, related_name='call_logs', null=True, blank=True)

    class Meta:
        constraints = (
            # for checking in the DB
            CheckConstraint(
                check=Q(paid__gte=0.0),
                name='call_log_paid_range'),
        )
