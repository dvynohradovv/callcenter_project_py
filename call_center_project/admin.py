from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from call_center_project.models import (Address, CallerPerson, CallLog, Office,
                                        OperatorToWorkPlace, Software,
                                        SoftwareVersion, TenantCompany,
                                        TenantCompanyPhoneNumber, User,
                                        WorkPlace)


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            # group heading of your choice; set to None for a blank space instead of a header
            'Custom Field Heading',
            {
                'fields': (
                    'type',
                    'isdisabled',
                    'gender',
                    'phone_number',
                    'tenant_company'
                ),
            },
        ),
    )


# Register your models here.
admin.site.register(Address)
admin.site.register(Office)
admin.site.register(Software)
admin.site.register(SoftwareVersion)
admin.site.register(WorkPlace)
admin.site.register(TenantCompany)
admin.site.register(TenantCompanyPhoneNumber)
admin.site.register(CallerPerson)
admin.site.register(User, CustomUserAdmin)
admin.site.register(OperatorToWorkPlace)
admin.site.register(CallLog)
