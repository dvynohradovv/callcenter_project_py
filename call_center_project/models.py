from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CheckConstraint, Q


class GenderType(models.TextChoices):
    Unknown = "Unknown"
    Other = "Other"
    Male = "Male"
    Female = "Female"


class AccountType(models.TextChoices):
    Unactive = "Unactive"
    Admin = "Admin"
    Operator = "Operator"
    TenantCompanyOwner = "TenantCompanyOwner"


class CategoryType(models.TextChoices):
    Unknown = "Unknown"
    Other = "Other"
    Production = "Production"
    Commerce = "Commerce"
    ServiceIndustry = "Service_Industry"


class DisconnectInitiatorType(models.TextChoices):
    Origination = "Origination"
    Operator = "Destination"


class ResponseType(models.TextChoices):
    Forbidden = "Forbidden"
    BusyHere = "BusyHere"
    RequestTerminated = "Request_Terminated"
    OK = "OK"


class Address(models.Model):
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    building = models.CharField(max_length=100, blank=True)
    additional_info = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return (
            f"{self.street}, {self.city}, {self.state} {self.zip_code}, {self.country}"
        )


class Office(models.Model):
    address = models.ForeignKey(
        "call_center_project.Address",
        models.SET_NULL,
        related_name="offices",
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["address", "title"], name="unique_office")
        ]

    def __str__(self) -> str:
        return f"{self.title} | {self.address}"


class Software(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return f"{self.title}"


class SoftwareVersion(models.Model):
    version = models.CharField(max_length=100)
    software = models.ForeignKey(
        "call_center_project.Software",
        on_delete=models.CASCADE,
        related_name="software_versions",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["version", "software"], name="unique_software_version"
            )
        ]

    def __str__(self) -> str:
        return f"{self.version} | {self.software}"


class WorkPlace(models.Model):
    room_number = models.CharField(max_length=100)
    office = models.ForeignKey(
        "call_center_project.Office", models.CASCADE, related_name="work_places"
    )
    software_version = models.ForeignKey(
        "call_center_project.SoftwareVersion",
        models.SET_NULL,
        related_name="work_places",
        null=True,
        blank=True,
    )
    tenant_company = models.ForeignKey(
        "call_center_project.TenantCompany",
        models.SET_NULL,
        related_name="work_places",
        null=True,
        blank=True,
    )
    operators = models.ManyToManyField(
        "call_center_project.User", through="OperatorToWorkPlace"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["room_number", "office"], name="unique_work_place"
            )
        ]

    def __str__(self) -> str:
        return f"{self.room_number} | {self.office} | {self.tenant_company}"


class TenantCompany(models.Model):
    isdisabled = models.BooleanField(default=False)
    title = models.CharField(max_length=100, unique=True)
    category = models.CharField(
        max_length=100, choices=CategoryType.choices, default=CategoryType.Unknown
    )
    price_per_operator = models.FloatField(blank=True)

    class Meta:
        constraints = (
            # for checking in the DB
            CheckConstraint(
                check=Q(price_per_operator__gte=0.0),
                name="tenant_company_price_per_operator_range",
            ),
        )

    def __str__(self) -> str:
        return f"{self.title}"


class TenantCompanyPhoneNumber(models.Model):
    phone_number = models.CharField(max_length=100, unique=True, null=True)
    tenant_company = models.ForeignKey(
        "call_center_project.TenantCompany",
        models.CASCADE,
        related_name="tenant_company_phone_numbers",
    )
    description = models.TextField(blank=True)
    isdisabled = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.tenant_company} | {self.phone_number}"


class CallerPerson(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, unique=True)
    gender = models.CharField(
        max_length=100, choices=GenderType.choices, default=GenderType.Unknown
    )
    email = models.EmailField(blank=True, null=True, default=None)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} | {self.phone_number}"


class User(AbstractUser):
    type = models.CharField(
        max_length=100, choices=AccountType.choices, default=AccountType.Unactive
    )
    isdisabled = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    gender = models.CharField(
        max_length=100, choices=GenderType.choices, default=GenderType.Unknown
    )
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    tenant_company = models.ForeignKey(
        "call_center_project.TenantCompany",
        models.SET_NULL,
        related_name="users",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.type} | {self.username}"

    @property
    def is_unactive(self):
        return self.type == AccountType.Unactive.value

    @property
    def is_admin(self):
        return self.type == AccountType.Admin.value

    @property
    def is_operator(self):
        return self.type == AccountType.Operator.value

    @property
    def is_tenant_company_owner(self):
        return self.type == AccountType.TenantCompanyOwner.value


class OperatorToWorkPlace(models.Model):
    operator = models.ForeignKey("call_center_project.User", models.CASCADE)
    work_place = models.ForeignKey("call_center_project.WorkPlace", models.CASCADE)


class CallLog(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveSmallIntegerField()
    caller_person = models.ForeignKey(
        "call_center_project.CallerPerson", models.CASCADE, related_name="call_logs"
    )
    caller_person_message = models.TextField(blank=True)
    tenant_company_phone_number = models.ForeignKey(
        "call_center_project.TenantCompanyPhoneNumber",
        models.CASCADE,
        related_name="call_logs",
    )
    operator = models.ForeignKey(
        "call_center_project.User", models.SET_NULL, related_name="call_logs", null=True
    )
    operator_message = models.TextField(blank=True)
    disconnect_initiator = models.CharField(
        max_length=100, choices=DisconnectInitiatorType.choices
    )
    response = models.CharField(max_length=100, choices=ResponseType.choices)
    paid = models.FloatField()
    address = models.ForeignKey(
        "call_center_project.Address",
        models.SET_NULL,
        related_name="call_logs",
        null=True,
        blank=True,
    )

    class Meta:
        constraints = (
            # for checking in the DB
            CheckConstraint(check=Q(paid__gte=0.0), name="call_log_paid_range"),
        )
